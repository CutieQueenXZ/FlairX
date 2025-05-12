import requests

def handle(comment):
    body = comment.body.lower()
    if body.startswith("!catfacts"):
        try:
            response = requests.get("https://catfact.ninja/fact").json()
            fact = response.get("fact", "Couldn't fetch a cat fact right now.")
            comment.reply(f"**Cat Fact:** {fact}")
        except Exception:
            comment.reply("Oops! Something went wrong while fetching a cat fact.")
