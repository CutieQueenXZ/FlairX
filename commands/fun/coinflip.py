import random

def handle(comment):
    if "!coinflip" in comment.body.lower():
        comment.reply(random.choice(["Heads!", "Tails!"]))
