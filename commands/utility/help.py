def handle(comment):
    if comment.body.strip().lower() == "!help":
        comment.reply("Here's a list of commands:\n\n"
                      "- `!joke`\n"
                      "- `!fact`\n"
                      "- `!meme`\n"
                      "- `!coinflip`\n"
                      "- `!eightball`\n"
                      "- `!hug`\n"
                      "- `!website <url>`\n"
                      "- `!rizz <style> <@user>`")
