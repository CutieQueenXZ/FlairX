from . import gemini

COMMAND_MODULES = [gemini, ask-gemini]

def handle_commands(comment):
    for module in COMMAND_MODULES:
        try:
            module.handle(comment)
        except Exception as e:
            print(f"[ai] Error handling {module.__name__}: {e}")
