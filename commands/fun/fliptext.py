# commands/fun/fliptext.py
def handle(comment):
    if comment.body.lower().startswith("!fliptext "):
        text = comment.body[10:]
        flipped = text.translate(str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
            "ɐqɔpǝɟƃɥᴉɾʞןɯuodbɹsʇnʌʍxʎz∀𐐒ƆᗡƎℲ⅁HIſʞ⅂WИOԀQЯS⊥UVWXYZ⇂ᄅƐㄣϛ9ㄥ860"
        ))[::-1]
        comment.reply(f"˙{flipped}")
