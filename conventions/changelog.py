from os import system
from utils import get_text
from utils import sanitize_as_empty_string
from utils import gen_co_author


def changelog_convention(co_author):
    tag, msg = get_text()
    tag = tag.upper()
    composed_message = "%s: %s\n" % (tag, msg)
    composed_message += gen_co_author(co_author)
    system("git commit -m '%s'" % composed_message)
