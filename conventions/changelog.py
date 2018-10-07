from os import system
from utils import get_text
from utils import change_if_none


def changelog_convention(co_author=''):
    tag, msg = get_text()
    tag = tag.upper()
    co_author = change_if_none(co_author)
    composed_message = """%s: %s\n\nCo-authored-by: """ % (tag, msg)
    system("git commit -m '%s%s'" % (composed_message, co_author))
