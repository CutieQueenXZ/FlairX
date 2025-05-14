# commands/fun/howgay.py
import random

def handle(comment):
    if comment.body.lower().startswith("!howgay"):
        percent = random.randint(0, 100)
        comment.reply(f"🌈 You are **{percent}% gay** 😳 (based on random percent, not real)")
