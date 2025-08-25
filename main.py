# main.py
import os
import praw
from dotenv import load_dotenv
from commands import handle_commands

# Try to import keep_alive only if it exists
try:
    from keep_alive import keep_alive
    USE_KEEP_ALIVE = True
except ImportError:
    USE_KEEP_ALIVE = False

load_dotenv()

def main():
    print(f"Bot started in r/{subreddits}...")
    for comment in subreddit.stream.comments(skip_existing=True):
        try:
            handle_commands(comment)
        except Exception as e:
            print(f"Error handling comment {comment.id}: {e}")

# Reddit setup
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD")
)

subreddits_env = os.getenv("SUBREDDITS", "")
subreddits = "+".join(s.strip() for s in subreddits_env.split(",") if s.strip())
subreddit = reddit.subreddit(subreddits)

if __name__ == "__main__":
    if USE_KEEP_ALIVE:  # Only for Replit users
        keep_alive()
    main()
