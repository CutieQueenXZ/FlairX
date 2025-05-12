import requests

def handle(comment):
    body = comment.body.lower()
    if body.startswith("!meme"):
        try:
            response = requests.get("https://meme-api.com/gimme").json()
            meme_url = response["url"]
            meme_title = response["title"]
            comment.reply(f"**{meme_title}**\n\n{meme_url}")
        except Exception:
            comment.reply("Oops! Couldn't fetch a meme right now.")
