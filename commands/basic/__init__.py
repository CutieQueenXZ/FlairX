from . import hello, define, quote

COMMAND_MODULES = [hello, define, quote]

def handle(comment):
    body = comment.body.lower()
    for module in COMMAND_MODULES:
        if hasattr(module, "handle"):
            try:
                module.handle(comment)
            except Exception as e:
                print(f"[facts] Error handling {module.__name__}: {e}")
