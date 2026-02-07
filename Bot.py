import os
import telebot
import requests
import feedparser
import random

# GitHub Secrets se keys fetch karna
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_KEY = os.getenv("CRICKET_API_KEY")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telebot.TeleBot(BOT_TOKEN)

def get_live_score():
    """CricketData API se live match ka score lana"""
    try:
        url = f"https://api.cricketdata.org/v1/currentMatches?apikey={API_KEY}"
        response = requests.get(url).json()
        matches = response.get('data', [])
        
        if matches:
            # Pehla active match uthana
            match = matches[0]
            score_msg = (
                f"🏏 *LIVE MATCH UPDATE*\n\n"
                f"🏆 *{match['name']}*\n"
                f"📊 *Status:* {match['status']}\n\n"
                f"🔥 Kya lagta hai kaun baazi marega? niche comment mein batao! 👇"
            )
            return score_msg
        return None
    except Exception as e:
        print(f"Score Error: {e}")
        return None

def get_latest_news():
    """Cricbuzz RSS se latest news uthana"""
    try:
        feed = feedparser.parse("https://www.cricbuzz.com/rss-feeds/cricket-news")
        if feed.entries:
            news = feed.entries[0]
            news_msg = (
                f"🚀 *BREAKING NEWS*\n\n"
                f"🔥 {news.title}\n\n"
                f"🔗 [Poori Khabar Padhein]({news.link})"
            )
            return news_msg
        return None
    except Exception as e:
        print(f"News Error: {e}")
        return None

def post_to_telegram():
    # 1. Live Score Bhejna
    score = get_live_score()
    if score:
        bot.send_message(CHAT_ID, score, parse_mode="Markdown")
    
    # 2. Latest News Bhejna
    news = get_latest_news()
    if news:
        bot.send_message(CHAT_ID, news, parse_mode="Markdown")
    
    # 3. Engagement Poll (Har baar naya sawal)
    poll_questions = [
        "Aaj match ka 'Hero' kaun hoga? ⭐",
        "Kya aaj koi 100 banayega? 🏏",
        "Aapki favorite team kaunsi hai? 😍",
        "Pitch kaisa khel rahi hai? 🏟️"
    ]
    bot.send_poll(
        CHAT_ID,
        question=random.choice(poll_questions),
        options=["Batsmen", "Bowlers", "All-rounders", "Toss decides"],
        is_anonymous=False
    )

if __name__ == "__main__":
    if BOT_TOKEN and CHAT_ID:
        post_to_telegram()
        print("✅ Telegram par updates bhej di gayi hain!")
    else:
        print("❌ Error: Secrets check karein (Token ya Chat ID missing hai)")

