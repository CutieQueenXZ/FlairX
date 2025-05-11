from commands import fun

def handle_comment(comment):
    if comment.author.name == os.getenv("REDDIT_USERNAME"):
        return  # Ignore itself

    fun.handle_fun_command(comment)
