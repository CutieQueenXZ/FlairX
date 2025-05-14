from . import help, website, weather, chatgpt

def handle_commands(comment):
    for module in [help, website, weather, chatgpt]:
        module.handle(comment)
