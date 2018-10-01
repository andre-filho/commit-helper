from os import system
from utils import get_text

def symphony_convention():
    tag, msg = get_text()
    tag = tag.capitalize()
    system("git commit -m '[%s] %s'" % (tag, msg))