import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Store your API key securely

def handle(comment):
    body = comment.body.lower()
    if body.startswith("!chatgpt"):
        prompt = comment.body[8:].strip()
        if not prompt:
            comment.reply("Please provide a prompt after `!chatgpt`.")
            return

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.7
            )
            answer = response['choices'][0]['message']['content'].strip()
            comment.reply(f"**ChatGPT says:**\n\n{answer}")
        except Exception as e:
            print("OpenAI error:", e)
            comment.reply("Sorry, something went wrong while contacting ChatGPT.")
