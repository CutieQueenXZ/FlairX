import random

RIZZ_STYLES = {
    "spicy": [
        "Are you a flame? Because you just lit up my heart.",
        "You must be lava, ‘cause you’re hot and dangerous.",
        "You’re so fine, you make jalapeños jealous."
    ],
    "nice": [
        "If kindness was a person, it would be you.",
        "You light up every room you walk into.",
        "You're not just beautiful, you're brilliant too."
    ],
    "normal": [
        "Are you a magician? Because whenever I look at you, everyone else disappears.",
        "Do you have a map? Because I just got lost in your eyes.",
        "You're the reason I look down at my phone and smile... then walk into a pole."
    ]
}

def handle(comment):
    body = comment.body.lower()
    if body.startswith("!rizz"):
        parts = body.split()
        if len(parts) >= 3:
            style = parts[1]
            target = parts[2]
            rizz_lines = RIZZ_STYLES.get(style, RIZZ_STYLES["normal"])
            rizz = random.choice(rizz_lines)
            comment.reply(f"{target}, {rizz}")
        else:
            comment.reply("Usage: `!rizz [spicy/nice/normal] [username]`")
