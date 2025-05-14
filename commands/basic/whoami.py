# commands/fun/whoami.py
def handle(comment):
    if comment.body.lower().strip() == "!whoami":
        author = comment.author
        comment.reply(f"👤 You are u/{author.name}.\n- Account Created: {author.created_utc}\n- Link Karma: {author.link_karma}\n- Comment Karma: {author.comment_karma}")
