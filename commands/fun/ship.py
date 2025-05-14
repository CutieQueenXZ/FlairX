# commands/fun/ship.py
def handle(comment):
    if comment.body.lower().startswith("!ship "):
        parts = comment.body[6:].split()
        if len(parts) >= 2:
            name1 = parts[0][:len(parts[0])//2]
            name2 = parts[1][len(parts[1])//2:]
            comment.reply(f"💘 Ship name: **{name1 + name2}**")
        else:
            comment.reply("Please provide two names to ship. Example: `!ship Alice Bob`")
