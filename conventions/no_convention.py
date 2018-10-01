from os import system
from utils import get_text

def just_message():
    msg = str(input("commit message: "))
    system("git commit -m '%s'" % msg.capitalize())
