import requests

def handle_commands(comment):
    body = comment.body.lower()
    if body.startswith("!catfacts"):
        print("Received !catfacts command")
        try:
            response = requests.get("https://catfact.ninja/fact")
            data = response.json()
            fact = data.get("fact", "Couldn't fetch a cat fact right now.")
            print("Cat Fact:", fact)

            comment.reply(f"**Random Cat Fact:**\n\n{fact}")
        except Exception as e:
            print("CATFACTS error:", e)
            comment.reply("Oops! Something went wrong while fetching a cat fact.")
