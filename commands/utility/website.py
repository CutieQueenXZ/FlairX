import requests

def handle(comment):
    if comment.body.lower().startswith("!website"):
        try:
            parts = comment.body.split()
            if len(parts) >= 2:
                url = parts[1]
                if not url.startswith("http"):
                    url = "http://" + url
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    comment.reply(f"The website **{url}** is **online!**")
                else:
                    comment.reply(f"The website **{url}** returned status code {response.status_code}")
            else:
                comment.reply("Please provide a URL, like `!website example.com`")
        except Exception:
            comment.reply("Oops! Couldn't check the website status.")
