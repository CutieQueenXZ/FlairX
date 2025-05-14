# commands/fun/quote.py
import random

quotes = [
    "Believe in yourself.",
    "Dream big, work hard.",
    "You are stronger than you think.",
    "Success is not final; failure is not fatal.",
    "Every day is a second chance."
]

def handle(comment):
    if comment.body.lower().strip() == "!quote":
        quote = random.choice(quotes)
        comment.reply(f"💬 **Quote:** {quote}")
