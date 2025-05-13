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
]

def handle(comment):
    body = comment.body.lower()
    if body.startswith("!bighug"):
        hug_line = random.choice(HUG_LINES)
        comment.reply(f"**{hug_line}**")

# Optional: You might want to define a 'command_name' for dynamic help generation
command_name = "bighug"
