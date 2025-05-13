from . import joke, hug, coinflip, eightball, meme, rizz, bighug, ping

COMMAND_MODULES = [joke, hug, coinflip, eightball, meme, rizz, bighug, ping]

def handle_commands(comment):
    body = comment.body.lower()
    for module in COMMAND_MODULES:
        if hasattr(module, "handle"):
            try:
                module.handle(comment)
            except Exception as e:
                print(f"Error handling {module.__name__}: {e}")
