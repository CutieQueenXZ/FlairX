# main.py
from core.reddit_client import reddit
from core.command_handler import handle_comment
import os

def main():
    subreddit = reddit.subreddit(os.getenv("SUBREDDIT"))
    print(f"FlairX is active in r/{os.getenv('SUBREDDIT')}...")

    for comment in subreddit.stream.comments(skip_existing=True):
        try:
            handle_comment(comment)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
