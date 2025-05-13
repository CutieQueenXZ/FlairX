import random

facts = [
    "Octopuses have three hearts.",
    "A group of flamingos is called a flamboyance.",
    "Bananas are technically berries!"
]

def handle(comment):
    if "!fact" in comment.body.lower():
        comment.reply(random.choice(facts))
