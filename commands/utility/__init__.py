from . import help, website

def handle_commands(comment):
    for module in [help, website]:
        module.handle(comment)
