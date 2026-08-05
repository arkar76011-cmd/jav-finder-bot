<div align="center">
  
# 🤖  jav-finder-bot

An asynchronous Telegram bot built with Python that fetches movies and series using actor names or IDs via custom APIs and presents watchable embed links

## 🌟 Key Features
* 🔎 **API Integration:** Asynchronously queries custom external API endpoints for actor/series details
* 📄 **Smart Pagination:** Renders search results in clean, managed batches of **5 items per page**
* ⏱️ **Cooldown & Anti-Spam System:**
  * Implements a **30-second delay** after every 2 consecutive pagination extensions (`Y` requests)
  * Enforces a **20-second cooldown** between new user search requests[cite: 1].
* 🎬 **Inline Web Playback:** Features a direct `Watch Now ▷` inline keyboard button linking directly to clean embed URLs

## 🛠️ Tech Stack
| Component | Technology | Description |
| :--- | :--- | :--- |
| **Language** | [Python 3.8+](https://www.python.org/) | Core language implementation |
| **Framework** | [python-telegram-bot](https://python-telegram-bot.org/) | Telegram Bot API Wrapper (v20+) |
| **HTTP Client** | [httpx](https://www.python-httpx.org/) | Asynchronous HTTP requests handler |
| **Config** | [python-dotenv](https://github.com/theskumar/python-dotenv) | Environment variables management |

## ⚙️ Configuration Setup
Create a `.env` file in the root directory of your project with the following keys
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyZ
API_URL=https://your-api-domain.com/search?q=

## 🚀 Quick Start Guide
1. Clone the Repository:
   git clone https://github.com/arkar76011-cmd/jav-finder-bot.git
   cd jav-finder-bot

2. Install Dependencies:
   pip install python-telegram-bot httpx python-dotenv

3. Run the Bot:
   python javfinder.py

## 💬 How to Use
1. Send `/start` to the bot on Telegram
2. Type an actor's name or code/ID
3. Bot replies with the first 5 results and an Inline Button
4. Reply with `Y` to load 5 more, or `N` to cancel the session
