from . import joke, fact, hug, coinflip, eightball

def handle_fun_command(comment):
    for module in [joke, fact, hug, coinflip, eightball]:
        module.handle(comment)
