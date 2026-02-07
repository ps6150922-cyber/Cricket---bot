import os
import telebot
import requests
import feedparser
import random

# Keys fetch karna
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_KEY = os.getenv("CRICKET_API_KEY")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telebot.TeleBot(BOT_TOKEN)

def post_updates():
    print("Updates tayyar kar raha hoon...")
    try:
        # 1. LIVE SCORE (Safe check ke saath)
        try:
            score_url = f"https://api.cricketdata.org/v1/currentMatches?apikey={API_KEY}"
            score_data = requests.get(score_url).json()
            matches = score_data.get('data', [])
            
            if matches:
                match = matches[0]
                score_text = f"🏏 *LIVE SCORE:* {match['name']}\n\n📊 Status: {match['status']}"
                bot.send_message(CHAT_ID, score_text, parse_mode="Markdown")
        except Exception as e:
            print(f"Score Skip (Limit Issue): {e}")

        # 2. LATEST NEWS
        feed = feedparser.parse("https://www.cricbuzz.com/rss-feeds/cricket-news")
        if feed.entries:
            news = feed.entries[0]
            news_text = f"🚀 *BREAKING:* {news.title}\n\n🔗 [Poori Khabar]({news.link})\n\n🔥 Comment mein batao kaisa laga!"
            bot.send_message(CHAT_ID, news_text, parse_mode="Markdown", disable_web_page_preview=False)

        # 3. ENGAGEMENT POLL (Fix: is_anonymous=True kiya hai channel ke liye)
        bot.send_poll(
            CHAT_ID,
            question="Aaj ka match kaun paltega? 🔥",
            options=["Batsmen", "Bowlers", "Luck/Toss", "Fielding"],
            is_anonymous=True  # Ye badlav zaroori tha
        )
        print("✅ Telegram par updates bhej di gayi hain!")

    except Exception as e:
        print(f"❌ Final Error: {e}")

if __name__ == "__main__":
    post_updates()
