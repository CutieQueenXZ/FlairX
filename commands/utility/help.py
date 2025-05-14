def handle(comment):
    if comment.body.strip().lower() == "!help":
        help_text = (
            "**FlairX Help Menu**\n\n"
            "**🧠 AI Command**\n"
            "`!gemini` - (temporarily broken which ai putted payment like chatgpt😥)\n\n"

            "**🎉 Fun Commands**\n"
            "`!joke` — Get a random joke\n"
            "`!rizz` — Get a rizz line\n"
            "`!coinflip` — Flip a coin\n"
            "`!eightball` — Ask the magic 8-ball\n"
            "`!hug u/username` — Send a hug\n"
            "`!bighug u/username` — Send a BIG hug\n"
            "`!meme` — Get a random meme\n"
            "`!ping` — Pong!\n"
            "`!reverse text` — Reverse your message (filtered)\n"
            "`!choose option1 or option2 or ...` — Let bot choose\n"
            "`!motivate` — Get a motivational quote\n"
            "`!compliment` — Receive a nice compliment\n"
            "`!insult` — Receive a funny insult\n"
            "`!truth` — Get a truth question\n"
            "`!dare` — Get a dare\n"
            "`!hello` — Say hi to the bot\n\n"

            "**🌐 Utility Commands**\n"
            "`!website` — View official FlairX website\n"
            "`!weather (city)` — Get current weather info\n\n"

            "**🐾 Animal Commands**\n"
            "`!cat` — Random cat image\n"
            "`!dog` — Random dog image\n"
            "`!birb` — Random bird image\n"
            "`!frog` — Random frog image\n"
            "`!duck` — Random duck image\n"
            "`!catfacts` — Random cat fact\n"
            "`!fact` — Random general fact\n\n"

            "➕ *More features coming soon!*\n"
            "🤖 *Created by u/gamerharun*"
        )
        comment.reply(help_text)
