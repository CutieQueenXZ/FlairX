from commands.fun import joke, rizz, fact, coinflip, eightball, hug, meme, catfacts, dog, cat, bighug
from commands.utility import help, website
from commands.facts import catfacts, fact

def handle_commands(comment):
    for module in [joke, rizz, fact, coinflip, eightball, hug, meme,
                   help, website, catfacts, fact]:
        module.handle(comment)
