from . import areyouokay, really725

COMMAND_MODULES = [areyouokay, really725]

def handle_commands(comment):
    for module in COMMAND_MODULES:
        try:
            module.handle(comment)
        except Exception as e:
            print(f"[ai] Error handling {module.__name__}: {e}")
