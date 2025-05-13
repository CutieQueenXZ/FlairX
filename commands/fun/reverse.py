def handle(comment):
    body = comment.body
    if body.lower().startswith("!reverse"):
        text = body.replace("!reverse", "").strip()
        if text:
            comment.reply(text[::-1])
        else:
            comment.reply("Please provide text to reverse.")
