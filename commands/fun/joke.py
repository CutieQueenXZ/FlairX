import random

jokes = [
    "Why did the bot go to school? To improve its 'syntax'!",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "404 joke not found!"
]

def handle(comment):
    if "!joke" in comment.body.lower():
        comment.reply(random.choice(jokes))
