def just_message():
    msg = str(input("commit message: "))
    composed = "%s\n" % msg.capitalize()
    return composed
