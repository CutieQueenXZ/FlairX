def handle(comment):
    if "!hug" in comment.body.lower():
        comment.reply(f"*{comment.author.name} gets a warm, snuggly hug!*")
