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
subreddits_env = os.getenv("SUBREDDITS", "")
subreddits = "+".join(s.strip() for s in subreddits_env.split(",") if s.strip())
subreddit = reddit.subreddit(subreddits)

def main():
    print(f"🤖 FlairX bot started in r/{subreddits}...")
    for comment in subreddit.stream.comments(skip_existing=True):
        try:
            handle_commands(comment)
        except Exception as e:
            print(f"⚠️ Error handling comment {comment.id}: {e}")

if __name__ == "__main__":
    main()
