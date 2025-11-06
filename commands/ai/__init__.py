from . import gemini, askgemini, mention_handler

COMMAND_MODULES = [gemini, askgemini, mention_handler]

def handle_commands(comment):
    for module in COMMAND_MODULES:
        try:
            module.handle(comment)
        except Exception as e:
            print(f"[ai] Error handling {module.__name__}: {e}")
