import random

CAT_FACTS = [
    "Cats sleep for around 13 to 16 hours a day!",
    "A group of cats is called a clowder.",
    "Cats can rotate their ears 180 degrees.",
    "The world’s oldest cat lived to be 38 years old.",
    "A cat’s nose print is as unique as a human fingerprint.",
    "Cats use their whiskers to detect if they can fit through a space.",
    "Adult cats only meow to communicate with humans.",
    "Cats have five toes on their front paws, but only four on the back.",
    "A cat can jump up to six times its length.",
    "Cats purr for self-healing as well as when they’re happy.",
    "Isaac Newton is credited with inventing the cat door.",
    "A cat’s brain is 90% similar to a human’s brain.",
    "Cats can make over 100 different sounds.",
    "The oldest known pet cat was found in a 9,500-year-old grave.",
    "Most cats don’t have eyelashes.",
    "Cats have a third eyelid called a ‘haw’.",
    "Black cats are considered good luck in Japan.",
    "The heaviest domestic cat on record weighed over 46 pounds.",
    "Some cats are allergic to humans!",
    "Cats can’t taste sweetness.",
    "The largest cat breed is the Maine Coon.",
    "Cats sweat through their paw pads.",
    "Calico cats are almost always female.",
    "A cat’s heart beats nearly twice as fast as a human’s.",
    "Whiskers are so sensitive, they can detect minor changes in the air.",
    "Cats use their tails for balance.",
    "A cat was once the mayor of an Alaskan town.",
    "Cats have a Jacobson’s organ that lets them “taste” scents.",
    "Each cat ear has 32 muscles that control the outer ear.",
    "A cat can run up to 30 miles per hour.",
    "Tabby is a coat pattern, not a breed.",
    "The average cat can hear sounds up to 65 kHz.",
    "Cats were worshipped in Ancient Egypt.",
    "A kitten's eyes always start out blue.",
    "Cats mark territory with the scent glands on their cheeks.",
    "Cats can move their eyes independently like chameleons—just a little.",
    "Male cats are more likely to be left-pawed.",
    "Cats walk like camels and giraffes: right feet first, then left.",
    "The world’s richest cat inherited $13 million.",
    "A cat’s purring may have healing properties for humans.",
    "Some cats can open doors and cabinets with their paws.",
    "Cats have fewer taste buds than dogs.",
    "The oldest cat breed is the Egyptian Mau.",
    "Cats dream while they sleep, just like humans.",
    "Orange cats are more likely to be male.",
    "In the Middle Ages, cats were associated with witches.",
    "Cats can survive falls from great heights thanks to their righting reflex.",
    "The smallest cat on record was only 2.75 pounds.",
    "A cat’s meow is a learned behavior to get human attention.",
    "Cats can be trained, but they prefer to train humans.",
    "Some cats go crazy for olives like they do catnip."
]

def handle(comment):
    body = comment.body.lower()
    if body.startswith("!catfacts"):
        print("catfacts command triggered")  # Add this line
        fact = random.choice(CAT_FACTS)
        comment.reply(f"**Cat Fact:** {fact}")
