import google.generativeai as genai
import os
from utility.memory import already_replied, mark_replied  # 👈 import memory helpers

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-flash-latest")

def handle(comment):
    body = comment.body
    if body.lower().startswith("!gemini"):
        # 🧩 Prevent duplicate replies
        if already_replied(comment.id):
            return

        prompt = body[len("!gemini"):].strip()
        if not prompt:
            comment.reply("Please include a prompt after `!gemini`. Example: `!gemini Tell me a joke`")
            mark_replied(comment.id)
            return

        try:
            response = model.generate_content(prompt)
            reply_text = response.text.strip() if response.text else "Gemini didn't return anything useful."
        except Exception as e:
            print("Gemini error:", e)
            reply_text = "Sorry, something went wrong while contacting Gemini."

        comment.reply(reply_text)
        mark_replied(comment.id)
