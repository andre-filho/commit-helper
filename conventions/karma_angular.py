from os import system
from utils import get_text
from utils import change_if_none


def angular_convention(co_author=''):
    tag, msg, context = get_text(context=True)
    tag = tag.lower()
    co_author = change_if_none(co_author)
    composed_message = """%s(%s): %s\n\nCo-authored-by:
""" % (tag, context, msg)
    system('git commit -m "%s%s"' % (composed_message, co_author))
