import os

# File where we store all replied comment IDs
MEMORY_FILE = "replied.txt"

# Make sure file exists
if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        pass

def already_replied(comment_id):
    """Check if this comment was already replied to"""
    with open(MEMORY_FILE, "r") as f:
        ids = set(f.read().splitlines())
    return comment_id in ids

def mark_replied(comment_id):
    """Mark this comment as replied"""
    with open(MEMORY_FILE, "a") as f:
        f.write(comment_id + "\n")
