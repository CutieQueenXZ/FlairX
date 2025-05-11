import random

responses = [
    "Yes.", "No.", "Maybe.", "Ask again later.",
    "Definitely.", "I wouldn't count on it."
]

def handle(comment):
    if "!8ball" in comment.body.lower():
        comment.reply(random.choice(responses))
