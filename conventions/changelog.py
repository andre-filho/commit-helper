from os import system
from utils import get_text


def changelog_convention(co_author=''):
    tag, msg = get_text()
    tag = tag.upper()
    composed_message = """%s: %s\n\nCo-authored-by: """ % (tag, context)
    system("git commit -m '%s%s'" % (composed_message, co_author))
