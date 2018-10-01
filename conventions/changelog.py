from os import system
from utils import get_text


def changelog_convention():
    tag, msg = get_text()
    tag = tag.upper()
    system("git commit -m '%s: %s'" % (tag, msg))
