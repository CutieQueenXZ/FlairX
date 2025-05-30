from . import dog, cat, birb, frog, duck

COMMAND_MODULES = [dog, cat, birb, frog, duck]

def handle_commands(comment):
    for module in COMMAND_MODULES:
        try:
            module.handle(comment)
        except Exception as e:
            print(f"[animals] Error handling {module.__name__}: {e}")
