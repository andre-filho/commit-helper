from os import system
from utils import get_text
from utils import sanitize_as_empty_string
from utils import gen_co_author


def angular_convention(co_author):
    tag, msg, context = get_text(context=True)
    tag = tag.lower()
    co_author = sanitize_as_empty_string(co_author)
    if context is '':
        composed_message = composed_message = "%s: %s\n" % (tag, msg)
    composed_message = "%s(%s): %s\n" % (tag, context, msg)
    composed_message += gen_co_author(co_author)
    system('git commit -m "%s"' % composed_message)
