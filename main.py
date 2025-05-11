from core.reddit_client import reddit, can_post  # Make sure can_post is imported
from core.command_handler import handle_comment
import os

def main():
    subreddits = os.getenv("SUBREDDITS").split(",")
    subreddit = reddit.subreddit("+".join([s.strip() for s in subreddits]))
    print(f"FlairX is active in: {', '.join(subreddits)}")

    for comment in subreddit.stream.comments(skip_existing=True):
        try:
            if not can_post(comment.subreddit):
                print(f"[!] Skipping r/{comment.subreddit} — No permission to post.")
                continue

            handle_comment(comment)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
