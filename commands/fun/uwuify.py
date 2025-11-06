import re

def handle(comment):
    if comment.body.lower().startswith("!uwuify"):
        args = comment.body.split()[1:]

        if not args:
            comment.reply("UwU what do you want me to tuwn into cutesy speech? >w<")
            return

        text = " ".join(args).lower()

        # 🔒 banned / filtered words (to avoid Reddit TOS violations)
        banned_words = [
            "fuck", "fuc", "fck", "fux", "shit", "bitch", "nigg", "slut", "whore",
            "dick", "dik", "cock", "cok", "pussy", "cum", "sperm", "semen", "rape",
            "penis", "vagina", "tits", "boob", "anal", "nude", "nsfw"
        ]

        # Replace banned words with [censored]
        for word in banned_words:
            pattern = re.compile(rf"{word}", re.IGNORECASE)
            text = pattern.sub("[censored]", text)

        # 🧸 uwuify transformation
        uwu = text.replace("r", "w").replace("l", "w").replace("R", "W").replace("L", "W")
        uwu = uwu.replace("no", "nyo").replace("No", "Nyo").replace("mo", "myo").replace("Mo", "Myo")

        # 🐾 reply
        reply_text = (
            f"✨ **UwUified:** `{uwu}` ✨\n\n"
            "*I'm a cute AI bot that tuwns youw wowds into UwU speech!*"
        )
        comment.reply(reply_text)
