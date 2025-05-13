import random
import re

def handle(comment):
    body = comment.body
    if body.lower().startswith("!choose "):
        choices = re.split(r",\s*|\s+or\s+|\s*\|\s*", body[8:].strip(), flags=re.IGNORECASE)
        choices = [c.strip() for c in choices if c.strip()]

        if len(choices) < 2:
            comment.reply("Please provide at least two options for me to choose from, separated by commas, 'or', or '|'.")
            return

        selection = random.choice(choices)
        comment.reply(f"I choose...\n# **{selection.upper()}**")
