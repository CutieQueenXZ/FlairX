import os
import praw
from dotenv import load_dotenv
from commands.fun import handle_fun_command

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
    user_agent=os.getenv("USER_AGENT"),
)

subreddit = reddit.subreddit(os.getenv("SUBREDDIT"))

def main():
    print(f"Bot started in r/{os.getenv('SUBREDDIT')}...")
    for comment in subreddit.stream.comments(skip_existing=True):
        try:
            handle_fun_command(comment)
        except Exception as e:
            print(f"Error handling comment {comment.id}: {e}")

if __name__ == "__main__":
    main()
