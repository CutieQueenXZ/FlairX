from commands.fun import joke, rizz, coinflip, eightball, hug, meme, bighug, cat
from commands.utility import help, website
from commands.facts import catfacts, fact

def handle_commands(comment):
    for module in [joke, rizz, fact, coinflip, eightball, hug, bighug, meme,
                   help, website, catfacts, cat]:
        module.handle(comment)
