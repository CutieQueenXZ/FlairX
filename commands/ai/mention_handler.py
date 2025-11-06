# commands/ai/mention_handler.py
import os
import re
from praw.models import Comment, Submission

# import the gemini helper from the commands package
from commands.ai.gemini import generate_gemini_response

# import memory helpers using package path; fallback to no-op if missing
try:
    from commands.utility.memory import already_replied, mark_replied
except Exception:
    try:
        from utility.memory import already_replied, mark_replied
    except Exception:
        def already_replied(_): return False
        def mark_replied(_): return None

# BOT mention can be configured via env var (e.g. "u/FlairXish")
BOT_MENTION = os.getenv("BOT_MENTION", "u/flairxish").lower()


def _extract_query(raw_text: str):
    """
    Extract the query and which flag was used (--post, --comment, --both).
    Returns (target_type, query_text) where target_type is 'post', 'comment', 'both', or None.
    """
    # prefer explicit flags
    m = re.search(r'--(post|comment|both)\s+(.+?)(?:\s+--|$)', raw_text, flags=re.IGNORECASE)
    if m:
        return m.group(1).lower(), m.group(2).strip()

    # fallback: no explicit flag, return (None, remaining text after mention)
    # remove mention token and common flags, whatever remains is query
    cleaned = re.sub(re.escape(BOT_MENTION), "", raw_text, flags=re.IGNORECASE)
    cleaned = re.sub(r'--(post|comment|both|brief|creative|ignore)', "", cleaned, flags=re.IGNORECASE)
    cleaned = cleaned.strip()
    return None, cleaned


def _get_context(mention, target_type):
    """Fetch appropriate context (post, parent comment, or both)."""
    try:
        submission = getattr(mention, "submission", None)
        parent = mention.parent() if hasattr(mention, "parent") else None
    except Exception:
        submission = None
        parent = None

    if target_type == "post" and isinstance(submission, Submission):
        return (submission.title or "") + "\n\n" + (submission.selftext or "")
    if target_type == "comment" and isinstance(parent, Comment) and hasattr(parent, "body"):
        return parent.body
    if target_type == "both":
        title = (submission.title or "") if isinstance(submission, Submission) else ""
        body = (submission.selftext or "") if isinstance(submission, Submission) else ""
        parent_text = parent.body if (parent and hasattr(parent, "body")) else ""
        return f"{title}\n\n{body}\n\nParent comment:\n{parent_text}"
    # nothing explicit requested — try to auto-detect
    if parent and hasattr(parent, "body"):
        return parent.body
    if submission:
        return (submission.title or "") + "\n\n" + (submission.selftext or "")
    return ""


def handle_mention(mention):
    """
    Main logic: processes a single Comment mention object.
    This will only reply when BOT_MENTION is present in the comment body.
    """
    if not mention or not hasattr(mention, "body"):
        return

    raw_body = mention.body or ""
    body_lower = raw_body.lower()

    # Only act if the bot is explicitly mentioned
    if BOT_MENTION not in body_lower:
        return

    # Avoid replying to the bot itself
    try:
        if mention.author and mention.author.name and mention.author.name.lower() == os.getenv("REDDIT_USERNAME", "").lower():
            return
    except Exception:
        pass

    # Prevent duplicate replies
    try:
        if already_replied(mention.id):
            return
    except Exception as e:
        print(f"[mention_handler] memory check error: {e}")

    # Determine style flags
    mode = "normal"
    if "--brief" in body_lower:
        mode = "brief"
    elif "--creative" in body_lower:
        mode = "creative"

    # Extract query and target
    target_type, query = _extract_query(raw_body)
    query = (query or "").strip()

    if not query:
        # user mentioned but didn't give a useful query
        try:
            mention.reply("⚠️ Please specify a valid command, e.g. `--post explain this` or `--comment summarize this`.")
            mark_replied(mention.id)
        except Exception as e:
            print(f"[mention_handler] failed to reply for missing query: {e}")
        return

    # Get the context depending on flags or auto-detect
    context_text = _get_context(mention, target_type)

    # Build prompt for Gemini
    prompt = f"Query: {query}\n\nContext:\n{context_text}\n\nMode: {mode}"

    # Generate response (safe wrapper)
    try:
        reply = generate_gemini_response(prompt, mode)
    except Exception as e:
        print(f"[mention_handler] generate error: {e}")
        reply = "⚠️ Sorry, I couldn't generate a reply right now."

    # Reply and mark memory
    try:
        mention.reply(reply)
        mark_replied(mention.id)
        print(f"[mention_handler] replied to {mention.id}")
    except Exception as e:
        print(f"[mention_handler] failed to reply: {e}")


# Provide the standard `handle(comment)` like other command modules so your main dispatcher can call it:
def handle(comment):
    handle_mention(comment)
