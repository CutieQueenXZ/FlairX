def handle(comment):
    if comment.body.lower().startswith("!ping"):
        comment.reply("Pong!")
