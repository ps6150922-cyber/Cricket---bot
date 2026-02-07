import os
import tweepy
import feedparser

# Secrets fetch karna
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# X Client Setup
client = tweepy.Client(
    consumer_key=API_KEY, consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
)

# Alternative RSS Feed (Google News India - Cricket)
RSS_URL = "https://news.google.com/rss/search?q=cricket+india&hl=hi&gl=IN&ceid=IN:hi"

def post_cricket_news():
    try:
        print("News dhund raha hoon...")
        feed = feedparser.parse(RSS_URL)
        
        if len(feed.entries) > 0:
            news = feed.entries[0]
            title = news.title
            link = news.link
            
            # Catchy Viral Post (Under 280 chars)
            tweet_text = (
                f"🏏 BADI KHABAR: {title}\n\n"
                f"Aapki kya rai hai? 👇\n\n"
                f"Poori details: {link}\n\n"
                f"#Cricket #TeamIndia #CricketUpdates"
            )
            
            # Character limit safety check
            if len(tweet_text) > 280:
                tweet_text = title[:150] + "... " + link

            # Final Tweeting
            response = client.create_tweet(text=tweet_text)
            print(f"✅ MUBARAK HO! Post ho gayi. Tweet ID: {response.data['id']}")
        else:
            print("❌ Error: News nahi mil pa rahi hai.")

    except Exception as e:
        print(f"❌ Error aagaya: {e}")

if __name__ == "__main__":
    post_cricket_news()
