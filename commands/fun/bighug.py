import random

HUG_LINES = [
    "A big warm hug for you!",
    "Here's a massive bear hug!",
    "Sending you the tightest virtual hug ever!",
    "You deserve a giant hug today!",
    "HUG ATTACK! You’ve been squeezed!",
    "Consider yourself embraced!",
    "A gentle hug coming your way.",
    "Wrapping you in a warm virtual embrace.",
    "Just wanted to send some huggles!",
    "A comforting hug from across the internet.",
    "May this virtual hug brighten your day!",
    "Sending you a super snuggly hug!",
    "Here's a hug filled with good vibes!",
    "Think of this as a warm embrace.",
    "A hug to make everything feel a little better.",
    "You're getting a big squeeze right now!",
    "Sending you a hug that lasts all day!",
    "Imagine a warm hug just for you.",
    "A virtual hug to chase away the blues.",
    "Consider yourself hugged and loved!",
    "Here's a hug as warm as the sun!",
    "Sending you a hug that knows no distance.",
    "A cozy hug to make you smile.",
    "You've been hugged by the internet!",
    "May this hug bring you comfort.",
    "Sending a hug with extra warmth!",
    "Here's a hug to make your day sweeter!",
    "Imagine a soft and gentle hug.",
    "A virtual hug just because!",
    "You're getting a big, comforting hug!"
]

def handle(comment):
    body = comment.body.lower()
    if body.startswith("!bighug"):
        hug_line = random.choice(HUG_LINES)
        comment.reply(f"**{hug_line}**")

# Optional: You might want to define a 'command_name' for dynamic help generation
command_name = "bighug"
