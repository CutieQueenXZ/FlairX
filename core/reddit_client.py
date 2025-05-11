def can_post(subreddit):
    try:
        # Try fetching subreddit rules (requires posting permission)
        rules = subreddit.rules()
        return True
    except Exception as e:
        print(f"[!] FlairX can't post in r/{subreddit.display_name}: {e}")
        return False
