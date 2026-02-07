import os
import tweepy
import feedparser

# GitHub Secrets se keys automatically fetch hongi
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN") # News fetch karne ke liye zaroori nahi, par safe rakhna achha hai

# X (Twitter) Client Setup
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Cricket News RSS Feed (Aap koi bhi cricket RSS use kar sakte hain)
RSS_URL = "https://feeds.feedburner.com/ndtvsports-cricket"

def post_cricket_news():
    try:
        # News fetch karna
        feed = feedparser.parse(RSS_URL)
        if not feed.entries:
            print("Nayi news nahi mili.")
            return

        # Sabse latest news uthana
        latest_news = feed.entries[0]
        title = latest_news.title
        link = latest_news.link

        # Tweet format karna
        tweet_text = f"🏏 Latest Cricket Update:\n\n{title}\n\nRead more: {link}\n\n#Cricket #CricketNews #Updates"

        # Tweet post karna
        response = client.create_tweet(text=tweet_text)
        print(f"Post successful! Tweet ID: {response.data['id']}")

    except Exception as e:
        print(f"Error aagaya: {e}")

if __name__ == "__main__":
    post_cricket_news()
