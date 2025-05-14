# commands/utility/define.py
import requests

def handle(comment):
    if comment.body.lower().startswith("!define "):
        word = comment.body[8:].strip()
        res = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if res.status_code == 200:
            data = res.json()[0]
            meaning = data['meanings'][0]['definitions'][0]['definition']
            comment.reply(f"📖 **{word}**: {meaning}")
        else:
            comment.reply(f"❌ Couldn't find a definition for '{word}'.")
