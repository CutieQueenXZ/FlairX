import os
import praw
from dotenv import load_dotenv
from commands.fun import handle_fun_command 
from commands.fun import handle_utility_command

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD")
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
