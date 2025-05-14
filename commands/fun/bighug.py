import random

bighug_lines = [
    "Here comes a SUPER BIG hug, {user}!",
    "A MASSIVE bear hug for you, {user}!",
    "The warmest, squishiest hug ever, {user}!",
    "Imagine the biggest teddy bear hug right now, {user}!",
    "Sending a galaxy-sized hug your way, {user}!",
    "A colossal embrace just for you, {user}!",
    "You're getting a hug that could lift a car, {user}!",
    "Wrapping you in virtual arms of steel (but with love!), {user}!",
    "Prepare for a hug that bends space and time, {user}!",
    "Consider yourself enveloped in pure hug energy, {user}!",
    "A hug so big, it needs its own zip code, {user}!",
    "Sending a hug that's bigger than your screen, {user}!",
    "You've just been hit by a hug wave, {user}!",
    "Here's a hug that's off the charts, {user}!",
    "Get ready for a hug that's out of this world, {user}!",
    "A hug that's stronger than gravity, just for you, {user}!",
    "Imagine a hug from a giant robot... a friendly one!, {user}",
    "You're receiving a hug of epic proportions, {user}!",
    "This hug has been supersized just for you, {user}!",
    "Consider yourself hugged with maximum intensity, {user}!",
    "A hug that could squeeze the stress right out of you, {user}!",
    "Sending a hug that's as wide as the horizon, {user}!",
    "You're getting a hug that's bursting with affection, {user}!",
    "Here's a hug that's overflowing with good vibes, {user}!",
    "Get ready for a hug that's pure comfort, {user}!",
    "A hug that's tailor-made for your awesomeness, {user}!",
    "Imagine a hug that lasts forever... or at least a good while!, {user}",
    "You're receiving a hug of legendary status, {user}!",
    "This hug comes with extra sprinkles of joy, {user}!",
    "Consider yourself embraced by pure happiness, {user}!",
    "A hug that's designed to make your day better, {user}!",
    "Sending a hug that's as warm as a summer day, {user}!",
    "You're getting a hug that's full of care, {user}!",
    "Here's a hug that's guaranteed to make you smile, {user}!",
    "Get ready for a hug that's simply the best, {user}!",
    "A hug that's powered by pure friendship, {user}!",
    "Imagine a hug that makes all your worries disappear, {user}!",
    "You're receiving a hug of ultimate coziness, {user}!",
    "This hug is brought to you with extra love, {user}!",
    "Consider yourself enveloped in a cloud of hug, {user}!",
    "A hug that's sent with the warmest intentions, {user}!",
    "Sending a hug that's as bright as the sun, {user}!",
    "You're getting a hug that's truly special, {user}!",
    "Here's a hug that's packed with positive energy, {user}!",
    "Get ready for a hug that's like a warm blanket, {user}!",
    "A hug that's a little piece of happiness for you, {user}!",
    "Imagine a hug that makes you feel completely safe, {user}!",
    "You're receiving a hug of pure delight, {user}!",
    "This hug comes with a side of good cheer, {user}!",
    "Consider yourself embraced by a force of hugitude, {user}!",
    "A hug that's meant to brighten your spirit, {user}!",
    "Sending a hug that's as comforting as a purr, {user}!",
    "You're getting a hug that's full of appreciation, {user}!",
    "Here's a hug that's just what you needed, {user}!",
    "Get ready for a hug that's simply wonderful, {user}!",
    "A hug that's sent with a smile, just for you, {user}!",
    "Imagine a hug that makes you feel completely understood, {user}!",
    "You're receiving a hug of pure kindness, {user}!",
    "This hug is delivered with extra care, {user}!",
    "Consider yourself enveloped in a hug of epic proportions, {user}!",
    "A hug that's designed to make your day fantastic, {user}!"
]

def handle(comment):
    body = comment.body.lower()
    if body.startswith("!bighug"):
        user = f"u/{comment.author.name}"
        line = random.choice(bighug_lines).format(user=user)
        comment.reply(f"**Big Hug!** {line}")

# Optional: You might want to define a 'command_name' for dynamic help generation
command_name = "bighug"
