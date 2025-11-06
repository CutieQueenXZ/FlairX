import google.generativeai as genai
import os
import re
from utility.memory import already_replied, mark_replied

# 🔑 Gemini setup
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-flash-latest")

# 🎨 Tone modifiers
MODIFIERS = {
    "normal": "",
    "brief": "Give a short, clear and to-the-point answer.",
    "creative": "Respond imaginatively, humorously or with flair.",
}

def generate_gemini_response(prompt: str, mode: str = "normal") -> str:
    """Generate a response using Gemini with the selected style."""
    try:
        full_prompt = f"{MODIFIERS.get(mode, '')}\n{prompt}"
        response = model.generate_content(full_prompt)
        return response.text.strip() if response.text else "🤔 Gemini returned no response."
    except Exception as e:
        print("⚠️ Gemini error:", e)
        return "❌ Sorry, Gemini couldn't respond due to an error."


def handle(comment):
    """Handles both !gemini commands and mentions like u/FlairXish --post ..."""
    body = comment.body.strip().lower()

    # ✅ Prevent duplicates
    if already_replied(comment.id):
        print(f"⏩ Already replied to {comment.id}")
        return

    # --- Case 1: !gemini prompt ---
    if body.startswith("!gemini"):
        prompt = comment.body[len("!gemini"):].strip()
        if not prompt:
            comment.reply("Please include a prompt after `!gemini`. Example: `!gemini Tell me a joke.`")
            mark_replied(comment.id)
            return

        reply = generate_gemini_response(prompt)
        comment.reply(reply)
        mark_replied(comment.id)
        return

    # --- Case 2: mention style (u/flairxish --post/--comment etc.) ---
    if "u/flairxish" in body:
        # detect target (post/comment)
        target_type = None
        if "--post" in body:
            target_type = "post"
        elif "--comment" in body:
            target_type = "comment"

        # detect mode (brief/creative)
        mode = "normal"
        if "--brief" in body:
            mode = "brief"
        elif "--creative" in body:
            mode = "creative"

        # extract query text
        match = re.search(r'--(?:post|comment)\s+(.+?)(?:\s+--|$)', comment.body, re.IGNORECASE)
        if not match:
            comment.reply("⚠️ Please specify a valid format, e.g. `u/flairxish --post explain this`.")
            mark_replied(comment.id)
            return

        query = match.group(1).strip()

        # get context (post text or parent comment)
        context_text = ""
        try:
            if target_type == "post":
                context_text = comment.submission.selftext or comment.submission.title
            elif target_type == "comment":
                parent = comment.parent()
                if hasattr(parent, "body"):
                    context_text = parent.body
        except Exception as e:
            print("⚠️ Context error:", e)

        prompt = f"User query: {query}\n\nContext:\n{context_text}\n\nMode: {mode}"
        reply = generate_gemini_response(prompt, mode)

        comment.reply(reply)
        mark_replied(comment.id)
        print(f"✅ Mention handled: {comment.id}")
