from . import joke, fact, hug, coinflip, eightball, meme, help, website, rizz

def handle_commands(comment):
    for module in [joke, fact, hug, coinflip, eightball, meme, help, website, rizz]:
        module.handle(comment)
