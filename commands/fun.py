import random

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the Reddit bot get fired? It couldn’t stop commenting!",
    "I would tell you a joke about UDP... but you might not get it.",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "I told my bot to be funny... it replied with '404 humor not found.'"
]

def handle_fun_command(comment):
    if "!joke" in comment.body.lower():
        joke = random.choice(jokes)
        comment.reply(joke)
