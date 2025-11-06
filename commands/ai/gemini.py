import google.generativeai as genai
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # or set manually

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-flash-latest")  # full model path

def handle(comment):
    body = comment.body
    if body.lower().startswith("!gemini"):
        prompt = body[len("!gemini"):].strip()
        if not prompt:
            comment.reply("Please include a prompt after `!gemini`. Example: `!gemini Tell me a joke`")
            return

        try:
            response = model.generate_content(prompt)
            reply_text = response.text.strip()
            if not reply_text:
                reply_text = "Gemini didn't return anything useful."
        except Exception as e:
            print("Gemini error:", e)
            reply_text = "Sorry, something went wrong while contacting Gemini."

        comment.reply(reply_text)
