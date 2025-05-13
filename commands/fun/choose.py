import random

def handle(comment):
    body = comment.body.lower()
    if body.startswith("!choose"):
        options = body.replace("!choose", "").strip().split(",")
        if len(options) > 1:
            choice = random.choice([opt.strip() for opt in options])
            comment.reply(f"I choose: **{choice}**")
        else:
            comment.reply("Please provide at least two options separated by commas.")
