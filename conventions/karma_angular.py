from os import system
from utils import get_text

def angular_convention():
    tag, msg, context = get_text(context=True)
    tag = tag.lower()
    system("git commit -m '%s(%s): %s'" % (tag, context, msg))
