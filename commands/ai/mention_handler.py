import re
from praw.models import Comment, Submission
from commands.ai.gemini import generate_gemini_response  # or your own helper
from utility.memory import already_replied, mark_replied

def handle_mention(mention, reddit):
    """Handle mentions like u/FlairXish --post explain this --creative"""

    body = mention.body.lower()
    if already_replied(mention.id):
        print(f"⏩ Already replied to mention {mention.id}")
        return

    # Detect command type
    target_type = None
    if "--post" in body:
        target_type = "post"
    elif "--comment" in body:
        target_type = "comment"

    # Detect mode
    mode = "normal"
    if "--brief" in body:
        mode = "brief"
    elif "--creative" in body:
        mode = "creative"

    # Extract query text
    match = re.search(r'--(?:post|comment)\s+(.+?)(?:\s+--|$)', body)
    if not match:
        mention.reply("⚠️ Please specify a valid command, e.g. `--post explain this` or `--comment summarize this`.")
        return

    query = match.group(1).strip()
    print(f"🧩 Mention detected: type={target_type}, mode={mode}, query={query}")

    # Fetch context (optional)
    context_text = ""
    if target_type == "post" and isinstance(mention.submission, Submission):
        context_text = mention.submission.selftext or mention.submission.title
    elif target_type == "comment" and isinstance(mention.parent(), Comment):
        context_text = mention.parent().body

    # Combine for better AI understanding
    prompt = f"Query: {query}\n\nContext:\n{context_text}\n\nMode: {mode}"

    # Generate Gemini response
    reply = generate_gemini_response(prompt, mode)

    # Reply back
    mention.reply(reply)
    mark_replied(mention.id)
    print(f"✅ Replied to mention {mention.id}")
