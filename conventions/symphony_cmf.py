from os import system
from utils import get_text


def symphony_convention(co_author=''):
    tag, msg = get_text()
    tag = tag.capitalize()
    composed = """[%s] %s\n\nCo-authored-by: """ % (tag, msg)
    system("git commit -m '%s%s'" % (composed, co_author))
