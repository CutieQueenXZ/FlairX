import requests

API_KEY = "5141c199f9f74dd18f6214929251305"

def handle(comment):
    body = comment.body.lower()
    if body.startswith("!weather "):
        city = body.replace("!weather ", "").strip()
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
        try:
            res = requests.get(url).json()
            temp = res['current']['temp_c']
            condition = res['current']['condition']['text']
            comment.reply(f"**Weather in {city.title()}**: {temp}°C, {condition}")
        except Exception:
            comment.reply("Sorry, I couldn't fetch the weather.")
