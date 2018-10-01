from os import system


def just_message():
    msg = str(input("commit message: "))
    system("git commit -m '%s'" % msg.capitalize())
