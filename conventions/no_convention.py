from os import system


def just_message(co_author=''):
    msg = str(input("commit message: "))
    composed = """%s\n\nCo-authored-by: """ % msg.capitalize()
    system("git commit -m '%s%s'" % (composed, co_author))
