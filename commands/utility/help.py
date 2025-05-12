def handle(comment):
    print(f"Received comment: {comment.body}")
    if comment.body.strip().lower() == "!help":
        print("Detected !help command")
        try:
            comment.reply("Here's a list of commands:\n\n"
                          "- `!joke`\n"
                          "- `!fact`\n"
                          "- `!meme`\n"
                          "- `!coinflip`\n"
                          "- `!eightball`\n"
                          "- `!hug`\n"
                          "- `!website <url>`\n"
                          "- `!rizz <style> <@user>`")
            print("Successfully replied to !help")
        except Exception as e:
            print(f"Error replying: {e}")
