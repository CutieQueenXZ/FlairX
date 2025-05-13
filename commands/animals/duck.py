import random

DUCK_IMAGES = [
    "https://random-d.uk/api/1.jpg",
    "https://random-d.uk/api/2.jpg",
    "https://random-d.uk/api/3.jpg",
]

def handle(comment):
    if comment.body.lower().startswith("!duck"):
        image = random.choice(DUCK_IMAGES)
        comment.reply(f"**Quack!** Here's a duck:\n\n{image}")
