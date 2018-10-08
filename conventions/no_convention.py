from os import system
from utils import change_if_none


def just_message(co_author=''):
    msg = str(input("commit message: "))
    co_author = change_if_none(co_author)
    composed = """%s\n\nCo-authored-by: """ % msg.capitalize()
    system("git commit -m '%s%s'" % (composed, co_author))
