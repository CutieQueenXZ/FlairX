import google.generativeai as genai
import os
import json

# === CONFIG ===
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MEMORY_FILE = "gemini_memory.json"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-flash-latest")

# === MEMORY SYSTEM ===
# Format: { thread_id: { "history": [...], "replied_ids": [] } }
try:
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
except FileNotFoundError:
    memory = {}

def save_memory():
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

# === COMMAND HANDLER ===
def handle(comment):
    body = comment.body.strip()
    if not body.lower().startswith("!ask-gemini"):
        return

    # Avoid duplicate replies
    thread_id = comment.submission.id
    comment_id = comment.id

    if thread_id not in memory:
        memory[thread_id] = {"history": [], "replied_ids": []}

    if comment_id in memory[thread_id]["replied_ids"]:
        print(f"[Gemini] Skipping duplicate reply in {thread_id}")
        return

    # === Parse Command ===
    args = body[len("!ask-gemini"):].strip().split()
    prompt_flags = [a for a in args if a.startswith("--")]
    user_prompt = " ".join(a for a in args if not a.startswith("--"))

    if not user_prompt:
        comment.reply(
            "🧠 Please include a question after `!ask-gemini`.\n"
            "Example: `!ask-gemini What is dark matter? --brief --comment`"
        )
        return

    # === Options ===
    mode = "none"
    if "--comment" in prompt_flags:
        mode = "comment"
    elif "--post" in prompt_flags:
        mode = "post"
    elif "--both" in prompt_flags:
        mode = "both"

    ignore_context = "--ignore" in prompt_flags
    brief = "--brief" in prompt_flags
    creative = "--creative" in prompt_flags

    # === Context & Memory ===
    context_text = ""
    if not ignore_context:
        try:
            post_title = comment.submission.title
            post_body = comment.submission.selftext or ""
            parent = None
            if mode in ("comment", "both"):
                parent = comment.parent()
                if parent and parent != comment.submission:
                    context_text += f"\nParent Comment:\n{parent.body[:1500]}"
            if mode in ("post", "both"):
                context_text += f"\nPost Title: {post_title}\nPost Body: {post_body[:2000]}"
        except Exception as e:
            print("Context fetch error:", e)

    history = "\n".join(memory[thread_id]["history"][-5:])  # last 5 only

    # === Build Prompt ===
    full_prompt = (
        f"Previous conversation:\n{history}\n\n"
        f"Context:\n{context_text}\n\n"
        f"User question: {user_prompt}\n\n"
    )

    if brief:
        full_prompt += "\nPlease give a concise 1-2 sentence answer."
    if creative:
        full_prompt += "\nBe imaginative and expressive with your tone."

    # === Generate Response ===
    try:
        response = model.generate_content(full_prompt)
        reply_text = response.text.strip() if response.text else "Gemini didn't return anything useful."

        # Save memory
        memory[thread_id]["history"].append(f"User: {user_prompt}")
        memory[thread_id]["history"].append(f"Gemini: {reply_text}")
        memory[thread_id]["replied_ids"].append(comment_id)
        save_memory()

    except Exception as e:
        print("Gemini error:", e)
        reply_text = "⚠️ Sorry, something went wrong while contacting Gemini."

    comment.reply(reply_text)
