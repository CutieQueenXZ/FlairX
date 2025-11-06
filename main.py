# main.py
import os
import time
import praw
from dotenv import load_dotenv
from commands import handle_commands
from keep_alive import keep_alive
from praw.exceptions import APIException, RedditAPIException, PRAWException

# 🧠 Load environment variables
load_dotenv()

# 🌐 Keep-alive webserver (for Replit/UptimeRobot)
keep_alive()

# 🦾 Reddit authentication
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD")
)

# 🎯 Subreddits (comma-separated in .env)
subreddits_env = os.getenv("SUBREDDITS", "FoundBob")
subreddits = "+".join(s.strip() for s in subreddits_env.split(",") if s.strip())
subreddit = reddit.subreddit(subreddits)


def main():
    print(f"🤖 FlairX bot started in r/{subreddits}...")
    last_seen = set()

    while True:
        try:
            # 💬 Fetch the latest comments
            for comment in subreddit.comments(limit=25):
                if comment.id not in last_seen:
                    last_seen.add(comment.id)

                    # Skip your own bot comments (avoid loops)
                    if comment.author and comment.author.name.lower() == os.getenv("REDDIT_USERNAME", "").lower():
                        continue

                    handle_commands(comment)

            # ⏱️ Avoid hitting Reddit’s API limits
            time.sleep(10)

        except (APIException, RedditAPIException) as e:
            print(f"⚠️ Reddit API exception: {e}")
            time.sleep(60)
        except PRAWException as e:
            print(f"⚙️ PRAW exception: {e}")
            time.sleep(30)
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            time.sleep(10)


if __name__ == "__main__":
    main()
