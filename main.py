# main.py
import os
import praw
from dotenv import load_dotenv
from commands import handle_commands
from keep_alive import keep_alive

load_dotenv()

# Start the small Flask webserver so UptimeRobot can ping it
keep_alive()

# Reddit authentication
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD")
)

# Support multiple subreddits like "funny,memes,test"
subreddits_env = os.getenv("SUBREDDITS", "FoundBob")
subreddits = "+".join(s.strip() for s in subreddits_env.split(",") if s.strip())
subreddit = reddit.subreddit(subreddits)

def main():
    print(f"🤖 FlairX bot started in r/{subreddits}...")
import time

def main():
    print(f"Bot started in r/{subreddits}...")
    last_seen = set()
    while True:
        try:
            for comment in subreddit.comments(limit=10):
                if comment.id not in last_seen:
                    last_seen.add(comment.id)
                    handle_commands(comment)
            time.sleep(10)
        except Exception as e:
            print(f"Error handling comment: {e}")
            time.sleep(5)
            
if __name__ == "__main__":
    main()
