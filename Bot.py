import os
import tweepy
import feedparser

# GitHub Secrets se keys fetch karna
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# X Client Setup
client = tweepy.Client(
    consumer_key=API_KEY, consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
)

# Active Cricket News Source
RSS_URL = "https://www.cricbuzz.com/rss-feeds/cricket-news"

def post_cricket_news():
    try:
        feed = feedparser.parse(RSS_URL)
        if len(feed.entries) > 0:
            title = feed.entries[0].title
            link = feed.entries[0].link
            
            # Catchy Tweet Format (Engagement ke liye)
            # Hum news ko short rakhenge aur ek sawal puchenge
            tweet_text = (
                f"🏏 BIG UPDATE: {title}\n\n"
                f"Aapko kya lagta hai is baare mein? 🤔\n\n"
                f"Poori khabar padhein 👇\n{link}\n\n"
                f"#Cricket #TeamIndia #CricketNews"
            )
            
            # Character check (X limit 280-300)
            if len(tweet_text) > 280:
                tweet_text = tweet_text[:270] + "..." + f"\n\n{link}"

            client.create_tweet(text=tweet_text)
            print(f"Post Success: {title}")
        else:
            print("News nahi mili!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    post_cricket_news()
