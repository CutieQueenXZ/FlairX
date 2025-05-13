import re

BANNED_WORDS = [
    # Racist/offensive
    "reggin", "reg-gin", "re.gg.in", "re ggin", "re+ggin",
    "regginlover", "duhc", "toohs", "kcuf", "hsurb", "rehton", "dnah", "ggub",
    "nigol", "reegn", "reyal", "nigger", "nigur", "suck my dick"

    # Sexual/inappropriate
    "sperm", "cum", "c*u*m", "c u m", "cu#", "c.u.m",
    "dick", "dic#", "d*ck", "d i c k",
    "sex", "s3x", "s.e.x", "s*x",
    "vagina", "vaj", "pussy", "p*ssy", "p u s s y",
    "f.u.c.k", "f*ck", "fu*k", "f u c k", "fuck", "dih", "pmo", "stfu", "ufts" 
]

def normalize(text):
    return re.sub(r'[^a-zA-Z]', '', text.lower())

def contains_banned(text):
    cleaned = normalize(text)
    return any(normalize(bad) in cleaned for bad in BANNED_WORDS)

def handle(comment):
    body = comment.body
    if body.lower().startswith("!reverse "):
        text_to_reverse = body[9:].strip()
        reversed_text = text_to_reverse[::-1]

        # Check both reversed and original text
        if contains_banned(text_to_reverse) or contains_banned(reversed_text):
            comment.reply("That reversed text looks inappropriate or violates rules, so I won't post it.")
            return

        comment.reply(
            f"**Reversed:** {reversed_text}\n\n"
            "*I'm an AI bot. The user asked for their message to be reversed. "
            "The creator (gamerharunyt) does not support any misuse or rule-breaking. "
            "For example, 'hello' becomes 'olleh'.*"
        )
