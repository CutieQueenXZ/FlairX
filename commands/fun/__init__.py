from . import joke, fact, hug, coinflip, eightball, meme

def handle_fun_command(comment):
    for module in [joke, fact, hug, coinflip, eightball, meme]:
        module.handle(comment)
