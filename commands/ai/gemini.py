import google.generativeai as genai
import os

# Load Gemini API key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def handle(comment):
    body = comment.body.strip()

    if body.lower().startswith("!gemini "):
        prompt = body[len("!gemini "):].strip()

        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            reply_text = response.text.strip()

            # Limit reply length to avoid Reddit limits
            if len(reply_text) > 1900:
                reply_text = reply_text[:1900] + "..."

            comment.reply(f"**Gemini says:**\n\n{reply_text}")
        except Exception as e:
            print(f"Gemini error: {e}")
            comment.reply("Sorry, something went wrong while contacting Gemini.")
