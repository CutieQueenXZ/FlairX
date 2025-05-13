from commands.fun import joke, rizz, coinflip, eightball, hug, meme, bighug
from commands.utility import help, website
from commands.facts import catfacts, fact

def handle_commands(comment):
    for module in [joke, rizz, fact, coinflip, eightball, hug, meme,
                   help, website, fact, catfacts]:
        module.handle(comment)
