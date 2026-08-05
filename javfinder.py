import os
import asyncio
import logging
import time
from pathlib import Path
import httpx
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)


env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = os.getenv("API_URL")

COOLDOWN_SECONDS = 20
user_cooldowns = {}
user_states = {}

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Enter actor name or ID.")

async def send_next_batch(update: Update, user_id: int):
    state = user_states.get(user_id)
    if not state or not state.get("results"):
        return

    results = state["results"]
    start_idx = state["index"]
    end_idx = start_idx + 5
    batch = results[start_idx:end_idx]

    if not batch:
        await update.message.reply_text("✅ No more results.")
        user_states.pop(user_id, None)
        return

    for title, clean_link in batch:
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Watch Now ▷", url=clean_link)]])
        await update.message.reply_text(f"📌 **{title}**", parse_mode="Markdown", reply_markup=keyboard)

    state["index"] = end_idx

    if state["index"] < len(results):
        state["awaiting_yn"] = True
        await update.message.reply_text("Fetch 5 more ? (Y/N)")
    else:
        await update.message.reply_text("✅ No more results.")
        user_states.pop(user_id, None)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    user_input = update.message.text.strip()

    if not user_input:
        return

    if user_id in user_states and user_states[user_id].get("awaiting_yn"):
        answer = user_input.upper()
        if answer == "Y":
            user_states[user_id]["awaiting_yn"] = False
            user_states[user_id]["y_count"] += 1

            if user_states[user_id]["y_count"] >= 2:
                wait_notice = await update.message.reply_text("⏳ Waiting 30s for 5 more...")
                await asyncio.sleep(30)
                try:
                    await wait_notice.delete()
                except Exception:
                    pass

            await send_next_batch(update, user_id)
            return
        elif answer == "N":
            await update.message.reply_text("🛑 Search cancelled")
            user_states.pop(user_id, None)
            return
        else:
            await update.message.reply_text("Enter 'Y' or 'N' only.")
            return

    current_time = time.time()
    if user_id in user_cooldowns:
        elapsed_time = current_time - user_cooldowns[user_id]
        if elapsed_time < COOLDOWN_SECONDS:
            remaining_time = COOLDOWN_SECONDS - elapsed_time
            wait_msg = await update.message.reply_text(
                f"⏳ Please wait {int(remaining_time)} seconds..."
            )
            await asyncio.sleep(remaining_time)
            try:
                await wait_msg.delete()
            except Exception:
                pass

    status_msg = await update.message.reply_text("🔎 Searching...")
    target_api_url = f"{API_URL}{user_input}"

    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.get(target_api_url)

            if response.status_code != 200:
                await status_msg.edit_text("❌ API connection failed.")
                return

            data = response.json()

        list_items = data.get("list", [])

        if not list_items:
            await status_msg.edit_text(
                "⚠️ No information found. Please recheck the correct code."
            )
            return

        extracted_links = []
        for item in list_items:
            title = item.get("name") or item.get("origin_name") or "No Title"
            episodes = item.get("episodes", {})
            server_data = episodes.get("server_data", {})
            full_data = server_data.get("Full", {})
            raw_embed_link = full_data.get("link_embed", "")

            if raw_embed_link:
                clean_link = raw_embed_link.replace("\\/", "/")
                extracted_links.append((title, clean_link))

        user_cooldowns[user_id] = time.time()

        if not extracted_links:
            await status_msg.edit_text("⚠️ `link_embed` No results found.")
            return

        await status_msg.delete()

        user_states[user_id] = {
            "results": extracted_links,
            "index": 0,
            "awaiting_yn": False,
            "y_count": 0
        }

        first_batch = extracted_links[:5]
        user_states[user_id]["index"] = 5

        for title, clean_link in first_batch:
            keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Watch Now ▷", url=clean_link)]])
            await update.message.reply_text(f"📌 **{title}**", parse_mode="Markdown", reply_markup=keyboard)

        if len(extracted_links) > 5:
            user_states[user_id]["awaiting_yn"] = True
            await update.message.reply_text("Fetch 5 more ? (Y/N)")

    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        await status_msg.edit_text(f"❌ An error has occurred: {str(e)}")

def main():
    if not BOT_TOKEN or not API_URL:
        raise ValueError("BOT_TOKEN or API_URL is missing! Please check your .env file.")
        
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()