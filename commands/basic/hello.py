def handle(comment):
    if comment.body.lower().startswith("!hello"):
        comment.reply("Hello there! wanna see !help ?")
