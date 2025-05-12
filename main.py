import os
import time
from dotenv import load_dotenv
from core.reddit_client import reddit, can_post
from commands.fun import handle_fun_command
load_dotenv()

def main():
    subreddits = os.getenv("SUBREDDITS").split(",")
    print(f"Monitoring subreddits: {subreddits}")

    for sub in subreddits:
        subreddit = reddit.subreddit(sub.strip())

        print(f"Starting stream in r/{sub.strip()}...")
        for comment in subreddit.stream.comments(skip_existing=True):
            try:
                # Basic filtering
                if comment.author == reddit.user.me():
                    continue  # Skip self
                if not can_post(comment.subreddit):
                    continue  # Custom check if the bot is allowed

                # Handle fun commands
                if comment.body.strip().startswith("!"):
                    handle_fun_command(comment)

            except Exception as e:
                print(f"Error processing comment: {e}")
                time.sleep(10)

if __name__ == "__main__":
    main()
