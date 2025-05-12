import requests

def handle(comment):
    body = comment.body.lower()
    if body.startswith("!dog"):
        try:
            response = requests.get("https://dog.ceo/api/breeds/image/random").json()
            image_url = response.get("message", "")
            comment.reply(f"Here's a random dog for you!\n\n{image_url}")
        except Exception:
            comment.reply("Oops! Couldn't fetch a dog image right now.")
