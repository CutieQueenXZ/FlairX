import os
import importlib

def handle(comment):
    if comment.body.strip().lower() == "!help":
        commands_path = os.path.dirname(__file__)  # Get the directory of help.py
        command_files = [f for f in os.listdir(commands_path) if f.endswith(".py") and f != "__init__.py" and f != "help.py"]
        command_list = "Here's a list of commands:\n"

        for filename in command_files:
            module_name = filename[:-3]  # Remove the .py extension
            try:
                module = importlib.import_module(f".{module_name}", package="commands")
                # Assuming each command module has a 'command_name' variable
                if hasattr(module, 'command_name'):
                    command_list += f"- !{module.command_name}\n"
                # Or, if you just want to use the filename as the command:
                # command_list += f"- !{module_name}\n"
            except ImportError as e:
                print(f"Error importing command module {module_name}: {e}")
                continue

        comment.reply(command_list)

# You might also need to define a 'command_name' variable in your other command files
# For example, in your joke.py:
# command_name = "joke"
