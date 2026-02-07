import os
import tweepy
import feedparser

# Keys fetch karna
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# X Client Setup
client = tweepy.Client(
    consumer_key=API_KEY, consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
)

# Naya 100% Working News Source (Google News Cricket)
RSS_URL = "https://news.google.com/rss/search?q=cricket+india&hl=en-IN&gl=IN&ceid=IN:en"

def post_cricket_news():
    try:
        feed = feedparser.parse(RSS_URL)
        
        if len(feed.entries) > 0:
            # Sabse taaza khabar uthana
            news = feed.entries[0]
            title = news.title
            link = news.link
            
            # Catchy Viral Format (Short & Engaging)
            tweet_text = (
                f"🏏 CRICKET FLASH: {title}\n\n"
                f"Is par aapka kya reaction hai? 👇\n\n"
                f"Read more: {link}\n\n"
                f"#Cricket #TeamIndia #CricketUpdates"
            )
            
            # Agar tweet 280 se bada hai to link ke liye jagah banana
            if len(tweet_text) > 280:
                tweet_text = title[:150] + "...\n\nRead more: " + link

            # Final Post
            client.create_tweet(text=tweet_text)
            print(f"Bhai, post ho gayi: {title}")
        else:
            print("Abhi bhi news nahi mili, link badalna hoga.")

    except Exception as e:
        print(f"Error aagaya: {e}")

if __name__ == "__main__":
    post_cricket_news()

