from commands.fun import joke, rizz, coinflip, eightball, hug, meme, bighug, ping, reverse, choose, motivate, compliment, insult, dadjoke
from commands.utility import help, website
from commands.facts import catfacts, fact
from commands.animals import cat, dog, birb, frog
from commands.basic import hello
def handle_commands(comment):
    for module in [joke, rizz, fact, coinflip, eightball, hug, bighug, meme,
                   help, website, catfacts, cat, dog, hello, ping, reverse,
                   choose, motivate, compliment, insult, dadjoke, birb, frog]:
        try:
            module.handle(comment)
        except Exception as e:
            print(f"[root] Error handling {module.__name__}: {e}")
