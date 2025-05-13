from . import fact, catfacts

COMMAND_MODULES = [fact, catfacts]

def handle_commands(comment):
    body = comment.body.lower()
    for module in COMMAND_MODULES:
        if hasattr(module, "handle"):
            try:
                module.handle(comment)
            except Exception as e:
                print(f"[facts] Error handling {module.__name__}: {e}")
