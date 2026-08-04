# 🎬 JAV Finder Telegram Bot

A Telegram Bot written in Python using `python-telegram-bot` and `httpx` for asynchronous search operations. It allows users to search for video information and embed links with pagination and automated rate-limiting cooldown controls.

## ✨ Features
- **Async Search:** Utilizes `httpx` for fast and non-blocking asynchronous HTTP requests.
- **Paginated Results:** Returns results in batches of 5 with confirmation prompts (`Y/N`) to fetch more.
- **User Cooldown Protection:** Built-in cooldown timer (20s) to prevent spam and rate-limiting issues.
- **Clean Output Formatting:** Formats video titles and embedded links with clean Markdown formatting.
- **Environment Variable Configuration:** Keeps sensitive bot tokens and API URLs safe using `.env` files.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Framework:** `python-telegram-bot`
- **HTTP Client:** `httpx`
- **Utilities:** `nest-asyncio`, `python-dotenv`

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/jav-finder-bot.git](https://github.com/YOUR_USERNAME/jav-finder-bot.git)
cd jav-finder-bot
