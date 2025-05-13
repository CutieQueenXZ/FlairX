from . import joke, fact, hug, coinflip, eightball, meme, rizz, catfacts, dog, cat, bighug

COMMAND_MODULES = [joke, fact, hug, coinflip, eightball, meme, rizz, catfacts, dog, cat, bighug]

def handle_commands(comment):
    body = comment.body.lower()
    for module in COMMAND_MODULES:
        if hasattr(module, "handle"):
            try:
                module.handle(comment)
            except Exception as e:
                print(f"Error handling {module.__name__}: {e}")
