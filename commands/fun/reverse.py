import re

BANNED_WORDS = [
    # Racist/abusive terms
    "reggin", "regginlover", "duhc", "toohs", "kcuf", "hsurb", "rehton",
    "dnah", "ggub", "reg-gin", "re.gg.in", "re ggin", "re+ggin",
    "nigol", "reegn", "reyal",
    
    # Sexual/inappropriate terms
    "sperm", "cum", "c*m", "c u m", "cu#", "c.u.m", "dick", "dic#", "d*ck", "d i c k",
    "sex", "s3x", "s.e.x", "s*x", "vagina", "vaj", "pussy", "p*ssy", "p u s s y"
]

def is_suspicious(text):
    # Normalize input to detect obfuscated variations
    cleaned = re.sub(r'[^a-zA-Z]', '', text).lower()
    for word in BANNED_WORDS:
        simplified = re.sub(r'[^a-zA-Z]', '', word.lower())
        if simplified in cleaned:
            return True
    return False

def handle(comment):
    body = comment.body
    if body.lower().startswith("!reverse "):
        text_to_reverse = body[9:].strip()
        reversed_text = text_to_reverse[::-1]

        if is_suspicious(reversed_text):
            comment.reply("That reversed text looks suspicious or inappropriate and isn’t allowed.")
            return

        comment.reply(
            f"**Reversed:** {reversed_text}\n\n"
            "*I'm an AI bot. The user asked for their message to be reversed. the creator(gamerharunyt) doesnt mean to make reddit rules to break."
            "For example, 'hello' becomes 'olleh'.*"
        )
