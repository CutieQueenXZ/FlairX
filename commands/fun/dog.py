import requests

def handle(comment):
    body = comment.body.lower()
    if body.startswith("!dog"):
        print("Received !dog command")
        try:
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            data = response.json()
            image_url = data.get("message", "")
            print("Dog image URL:", image_url)

            # Add more context to avoid Reddit filtering the reply
            comment.reply(f"**Woof!** Here's a cute dog for you:\n\n{image_url}")
        except Exception as e:
            print("DOG error:", e)
            comment.reply("Oops! Couldn't fetch a dog image right now.")
