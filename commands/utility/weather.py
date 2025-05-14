import requests
import os

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")  # set this in your .env or Railway variables

WEATHER_EMOJIS = {
    "sunny": "☀️",
    "clear": "🌕",
    "cloud": "☁️",
    "rain": "🌧️",
    "drizzle": "🌦️",
    "snow": "❄️",
    "storm": "⛈️",
    "fog": "🌫️",
    "mist": "🌫️",
    "overcast": "☁️",
    "thunder": "⛈️"
}

def get_weather_emoji(condition_text):
    text = condition_text.lower()
    for keyword, emoji in WEATHER_EMOJIS.items():
        if keyword in text:
            return emoji
    return "🌡️"

def handle(comment):
    body = comment.body.lower()
    if body.startswith("!weather"):
        parts = body.split(" ", 1)
        if len(parts) < 2:
            comment.reply("Please specify a location. Example: `!weather Warsaw`")
            return

        location = parts[1].strip()
        url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={location}&aqi=no"

        try:
            response = requests.get(url)
            data = response.json()

            if "error" in data:
                comment.reply(f"Could not fetch weather for '{location}'. Please check the location name.")
                return

            location_name = data['location']['name']
            country = data['location']['country']
            temp_c = data['current']['temp_c']
            feels_like = data['current']['feelslike_c']
            condition = data['current']['condition']['text']
            humidity = data['current']['humidity']
            wind_kph = data['current']['wind_kph']

            emoji = get_weather_emoji(condition)

            reply = (
                f"**Weather in {location_name}, {country}** {emoji}\n\n"
                f"- Temperature: {temp_c}°C\n"
                f"- Feels like: {feels_like}°C\n"
                f"- Condition: {condition}\n"
                f"- Humidity: {humidity}%\n"
                f"- Wind: {wind_kph} km/h"
            )
            comment.reply(reply)

        except Exception as e:
            print("Weather command error:", e)
            comment.reply("Sorry, I couldn't fetch the weather due to a system error.")
