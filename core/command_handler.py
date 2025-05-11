import os
from commands.fun import handle_fun_command

def handle_comment(comment):
    if comment.author.name == os.getenv("REDDIT_USERNAME"):
        return
    handle_fun_command(comment)
