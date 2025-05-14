from . import help, website, weather

def handle_commands(comment):
    for module in [help, website, weather]:
        module.handle(comment)
