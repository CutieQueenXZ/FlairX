# core/reddit_client.py
import praw
import os

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
)

def can_post(subreddit):
    try:
        _ = subreddit.rules()  # If this fails, likely can't post
        return True
    except Exception as e:
        print(f"[x] Can't access r/{subreddit.display_name} rules: {e}")
        return False
