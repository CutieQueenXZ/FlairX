from commands.fun import joke, rizz, coinflip, eightball, hug, meme, bighug, ping, reverse, choose, motivate, compliment, insult, dadjoke, truth, dare, fliptext, howgay, ship
from commands.utility import help, website, weather
from commands.facts import catfacts, fact
from commands.animals import cat, dog, birb, frog, duck
from commands.basic import hello, define, quote, whoami
from commands.ai import gemini
from commands.as182 import areyouokay, really725
def handle_commands(comment):
    for module in [joke, rizz, fact, coinflip, eightball, hug, bighug, meme,
                   help, website, catfacts, cat, dog, hello, ping, reverse,
                   choose, motivate, compliment, insult, dadjoke, birb, frog, duck,
                   weather, truth, dare, gemini, fliptext, howgay, ship, quote,
                   whoami, uwuify, areyouokay, really725]:
        try:
            module.handle(comment)
        except Exception as e:
            print(f"[root] Error handling {module.__name__}: {e}")
