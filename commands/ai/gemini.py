# commands/ai/gemini.py
import os
import re

# Try to import Gemini SDK (may be missing in some envs)
try:
    import google.generativeai as genai
except Exception:
    genai = None

# Memory helpers: try both common paths so imports don't break depending on layout
try:
    from commands.utility.memory import already_replied, mark_replied
except Exception:
    try:
        from utility.memory import already_replied, mark_replied
    except Exception:
        # Fallback no-op memory if the module isn't present
        def already_replied(comment_id):
            return False
        def mark_replied(comment_id):
            return None

# === Gemini setup ===
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.0-flash-lite")  # safer default for hobby use

if genai and GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
    except Exception as e:
        print(f"[gemini] warning: failed to configure API key: {e}")
else:
    if genai is None:
        print("[gemini] warning: google.generativeai SDK not installed.")
    elif not GEMINI_API_KEY:
        print("[gemini] warning: GEMINI_API_KEY not set in environment.")


# Tone/instruction modifiers
MODIFIERS = {
    "normal": "",
    "brief": "Give a short, clear and to-the-point answer.",
    "creative": "Respond imaginatively, humorously or with flair.",
}


def generate_gemini_response(prompt: str, mode: str = "normal") -> str:
    """
    Generate a response from Gemini. Returns a user-friendly error string on failure.
    """
    if genai is None:
        return "⚠️ Gemini SDK not installed on this host."
    if not GEMINI_API_KEY:
        return "⚠️ Gemini API key not configured. Add GEMINI_API_KEY to your environment."

    instruction = MODIFIERS.get(mode, "")
    full_prompt = (instruction + "\n\n" + prompt).strip()

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        resp = model.generate_content(full_prompt)
        # Typical SDK exposes .text; handle common cases
        if hasattr(resp, "text") and resp.text:
            return resp.text.strip()
        # Some responses may have candidates or other structure
        if hasattr(resp, "candidates") and resp.candidates:
            # join candidate texts if present
            texts = [c.text for c in resp.candidates if hasattr(c, "text")]
            if texts:
                return "\n\n".join(t.strip() for t in texts if t)
        return "🤔 Gemini returned an empty response."
    except Exception as e:
        print(f"[gemini] generation error: {e}")
        return "⚠️ Sorry, I couldn't reach Gemini right now. Try again later."


def handle(comment):
    """
    Handles both:
      - '!gemini <prompt>'
      - mention style: 'u/FlairXish --post <q>' or 'u/FlairXish --comment <q>' with flags --brief / --creative
    """
    if not comment or not hasattr(comment, "body"):
        return

    raw_body = comment.body or ""
    body_lower = raw_body.strip().lower()

    # Prevent duplicate replies
    try:
        if already_replied(comment.id):
            # print for debug
            print(f"[gemini] already replied to {comment.id}")
            return
    except Exception as e:
        print(f"[gemini] memory check error: {e}")

    # CASE A: !gemini command
    if body_lower.startswith("!gemini"):
        prompt = raw_body[len("!gemini"):].strip()
        if not prompt:
            try:
                comment.reply("Please include a prompt after `!gemini`. Example: `!gemini Tell me a joke.`")
                mark_replied(comment.id)
            except Exception as e:
                print(f"[gemini] reply error: {e}")
            return

        reply = generate_gemini_response(prompt, "normal")
        try:
            comment.reply(reply)
            mark_replied(comment.id)
        except Exception as e:
            print(f"[gemini] failed to reply to !gemini: {e}")
        return

    # CASE B: mention-style invocation (e.g. "u/FlairXish --post explain this --brief")
    # detect mention of bot username (case-insensitive). Change this string if your bot username differs.
    BOT_MENTION = os.getenv("BOT_MENTION", "u/flairxish").lower()
    if BOT_MENTION in body_lower:
        # parse flags
        target_type = None
        if "--post" in body_lower:
            target_type = "post"
        elif "--comment" in body_lower:
            target_type = "comment"
        elif "--both" in body_lower:
            target_type = "both"

        mode = "normal"
        if "--brief" in body_lower:
            mode = "brief"
        elif "--creative" in body_lower:
            mode = "creative"

        # extract query after the chosen flag; fall back to text after mention if none
        match = re.search(r'--(?:post|comment|both)\s+(.+?)(?:\s+--|$)', raw_body, re.IGNORECASE)
        if match:
            query = match.group(1).strip()
        else:
            # fallback: remove mention and known flags, remaining text is query
            query = raw_body
            for token in [BOT_MENTION, "--post", "--comment", "--both", "--brief", "--creative", "--ignore"]:
                query = re.sub(re.escape(token), "", query, flags=re.IGNORECASE)
            query = query.strip()

        if not query:
            try:
                comment.reply("⚠️ Please include a query. Example: `u/FlairXish --post explain this --brief`")
                mark_replied(comment.id)
            except Exception as e:
                print(f"[gemini] reply error: {e}")
            return

        # build context
        context_text = ""
        try:
            submission = comment.submission if hasattr(comment, "submission") else None
            parent = comment.parent() if hasattr(comment, "parent") else None

            if target_type == "post" and submission:
                context_text = (submission.selftext or submission.title or "")[:3000]
            elif target_type == "comment" and parent and hasattr(parent, "body"):
                context_text = parent.body[:3000]
            elif target_type == "both" and submission:
                part = (submission.title or "") + "\n\n" + (submission.selftext or "")
                parent_text = parent.body if parent and hasattr(parent, "body") else ""
                context_text = (part + "\n\n" + parent_text)[:4000]
            else:
                # if no explicit flag, try to auto-detect: prefer parent comment if exists
                if parent and hasattr(parent, "body"):
                    context_text = parent.body[:3000]
                elif submission:
                    context_text = (submission.title + "\n\n" + (submission.selftext or ""))[:3000]
        except Exception as e:
            print(f"[gemini] context fetch error: {e}")

        prompt = f"User query: {query}\n\nContext:\n{context_text}\n\nMode: {mode}"

        reply = generate_gemini_response(prompt, mode)

        try:
            comment.reply(reply)
            mark_replied(comment.id)
            print(f"[gemini] replied to mention {comment.id}")
        except Exception as e:
            print(f"[gemini] failed to reply to mention: {e}")

        return

    # If no recognized trigger, do nothing
    return
