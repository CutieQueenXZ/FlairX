import random

DOG_IMAGES = [
    "https://images.dog.ceo/breeds/shiba/shiba-13.jpg",
    "https://images.dog.ceo/breeds/labrador/n02099712_685.jpg",
    "https://images.dog.ceo/breeds/husky/n02110185_1469.jpg",
    "https://images.dog.ceo/breeds/beagle/n02088364_11136.jpg",
    "https://images.dog.ceo/breeds/pug/n02110958_15452.jpg",
    "https://images.dog.ceo/breeds/germanshepherd/n02106662_2740.jpg",
    "https://images.dog.ceo/breeds/terrier-silky/n02097658_3207.jpg",
    "https://images.dog.ceo/breeds/cockapoo/Scout.jpg",
    "https://images.dog.ceo/breeds/spaniel-cocker/n02102318_5690.jpg",
    "https://images.dog.ceo/breeds/akita/512px-Akita_inu.jpeg",
    "https://images.dog.ceo/breeds/terrier-border/n02093754_3375.jpg",
    "https://images.dog.ceo/breeds/boxer/n02108089_1298.jpg",
    "https://images.dog.ceo/breeds/malamute/n02110063_1122.jpg",
    "https://images.dog.ceo/breeds/papillon/n02086910_5396.jpg",
    "https://images.dog.ceo/breeds/doberman/n02107166_4912.jpg",
    "https://images.dog.ceo/breeds/mix/Golden_puppy.jpg",
    "https://images.dog.ceo/breeds/terrier-yorkshire/n02094433_4513.jpg",
    "https://images.dog.ceo/breeds/rottweiler/n02106550_9437.jpg",
    "https://images.dog.ceo/breeds/whippet/n02091134_3062.jpg",
    "https://images.dog.ceo/breeds/kuvasz/n02104029_3815.jpg",
    "https://images.dog.ceo/breeds/kelpie/n02105412_7411.jpg",
]

def handle(comment):
    body = comment.body.lower()
    if body.startswith("!dog"):
        image_url = random.choice(DOG_IMAGES)
        comment.reply(f"**Woof!** Here's a cute dog for you:\n\n{image_url}")
