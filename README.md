<div align="center">

  # 🎬 jav-finder-bot

  <p>
    An asynchronous Telegram bot built with Python that fetches movies and series using actor names or IDs via custom APIs and presents watchable embed links.
  </p>

  <!-- Badges -->
  <p>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version"></a>
    <a href="https://github.com/python-telegram-bot/python-telegram-bot"><img src="https://img.shields.io/badge/Telegram--Bot-v20.x-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Bot API"></a>
    <a href="https://www.python-httpx.org/"><img src="https://img.shields.io/badge/HTTPX-Async-0055ff?style=for-the-badge" alt="HTTPX"></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License"></a>
  </p>

</div>

---

## 🌟 Key Features

* 🔎 **API Integration:** Asynchronously queries custom external API endpoints for actor/series details.
* 📄 **Smart Pagination:** Renders search results in clean, managed batches of **5 items per page**.
* ⏱️ **Cooldown & Anti-Spam System:**
  * Implements a **30-second delay** after every 2 consecutive pagination extensions (`Y` requests).
  * Enforces a **20-second cooldown** between new user search requests.
* 🎬 **Inline Web Playback:** Features a direct `Watch Now ▷` inline keyboard button linking directly to clean embed URLs.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Language** | [Python 3.8+](https://www.python.org/) | Core language implementation |
| **Framework** | [python-telegram-bot](https://python-telegram-bot.org/) | Telegram Bot API Wrapper (v20+) |
| **HTTP Client** | [httpx](https://www.python-httpx.org/) | Asynchronous HTTP requests handler |
| **Config** | [python-dotenv](https://github.com/theskumar/python-dotenv) | Environment variables management |

---

## ⚙️ Configuration Setup

Create a `.env` file in the root directory of your project with the following keys[cite: 1]:

```env
# Telegram Bot Token from @BotFather
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyZ

# External Search API Base URL
API_URL=[https://your-api-domain.com/search?q=](https://your-api-domain.com/search?q=)


🚀 Quick Start Guide

1️⃣ Clone the Repository
Bash
git clone [https://github.com/arkar76011-cmd/jav-finder-bot.git](https://github.com/arkar76011-cmd/jav-finder-bot.git)
cd jav-finder-bot

2️⃣ Install Dependencies
Bash
pip install python-telegram-bot httpx python-dotenv

3️⃣ Run the Bot
Bash
python javfinder.py

💬 How to Use
Code snippet
1. Send `/start` to the bot on Telegram.
2. Type an actor's name or code/ID.
3. Bot replies with the first 5 results and an Inline Button.
4. Reply with 'Y' to load 5 more, or 'N' to cancel the session.
