import random

BIRB_IMAGES = [
    "https://random.birb.pics/img/birb1.jpg",
    "https://random.birb.pics/img/birb2.jpg",
    "https://random.birb.pics/img/birb3.jpg",
]

def handle(comment):
    if comment.body.lower().startswith("!birb"):
        image = random.choice(BIRB_IMAGES)
        comment.reply(f"**Birb Alert!**\n\n{image}")
