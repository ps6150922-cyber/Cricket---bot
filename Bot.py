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
    print("News dhund raha hoon...")
    try:
        # 1. LIVE SCORE (Agar API key khatam ho gayi hai toh ye skip ho jayega)
        try:
            score_url = f"https://api.cricketdata.org/v1/currentMatches?apikey={API_KEY}"
            score_data = requests.get(score_url).json()
            matches = score_data.get('data', [])
            
            if matches:
                match = matches[0]
                score_text = f"🏏 *LIVE SCORE:* {match['name']}\n\n📊 Status: {match['status']}"
                bot.send_message(CHAT_ID, score_text, parse_mode="Markdown")
        except Exception as e:
            print(f"Score Fetch Failed (Quota Issue): {e}")

        # 2. LATEST NEWS (Ye hamesha free rahega)
        feed = feedparser.parse("https://www.cricbuzz.com/rss-feeds/cricket-news")
        if feed.entries:
            news = feed.entries[0]
            news_text = f"🚀 *BREAKING:* {news.title}\n\n🔗 [Poori Khabar]({news.link})\n\n🔥 Comment mein batao kaisa laga!"
            bot.send_message(CHAT_ID, news_text, parse_mode="Markdown")

        # 3. ENGAGEMENT POLL
        bot.send_poll(
            CHAT_ID,
            question="Aaj ka match kaun paltega? 🔥",
            options=["Batsmen", "Bowlers", "Luck/Toss", "Fielding"],
            is_anonymous=False
        )
        print("✅ Telegram par updates bhej di gayi hain!")

    except Exception as e:
        print(f"❌ Final Error: {e}")

if __name__ == "__main__":
    post_updates()
