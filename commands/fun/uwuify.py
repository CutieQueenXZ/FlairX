def run(comment, args):
    if not args:
        comment.reply("UwU what do you want me to tuwn into cutesy speech? >w<")
        return
    text = " ".join(args)
    uwu = text.replace("r", "w").replace("l", "w").replace("R", "W").replace("L", "W")
    uwu = uwu.replace("no", "nyo").replace("No", "Nyo").replace("mo", "myo").replace("Mo", "Myo")
    comment.reply(f"✨ UwUified: `{uwu}` ✨")
