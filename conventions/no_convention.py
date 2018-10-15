from os import system
from utils import sanitize_as_empty_string
from utils import gen_co_author


def just_message(co_author):
    msg = str(input("commit message: "))
    composed = "%s\n" % msg.capitalize()
    composed += gen_co_author(co_author)
    system("git commit -m '%s'" % composed)
