import random

FROG_IMAGES = [
    "https://somefrogs.com/img/frog1.jpg",
    "https://somefrogs.com/img/frog2.jpg",
    "https://somefrogs.com/img/frog3.jpg",
]

def handle(comment):
    if comment.body.lower().startswith("!frog"):
        comment.reply(f"**Here's a frog!**\n\n{random.choice(FROG_IMAGES)}")
