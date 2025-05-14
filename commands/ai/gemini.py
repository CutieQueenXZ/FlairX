import google.generativeai as genai
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # or hardcode for testing

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")

def handle(comment):
    body = comment.body.lower()
    if body.startswith("!gemini"):
        prompt = comment.body[len("!gemini"):].strip()

        try:
            response = model.generate_content(prompt)
            reply_text = response.text.strip()
            if not reply_text:
                reply_text = "Gemini didn't return any content."
        except Exception as e:
            print("Gemini error:", e)
            reply_text = "Sorry, something went wrong while contacting Gemini."

        comment.reply(reply_text)
