from commit_helper.utils.colors import INPUT_COLOR
from commit_helper.utils.colors import RESET


def just_message():
    msg = str(input(INPUT_COLOR + "commit message: " + RESET))
    composed = "%s\n" % msg.capitalize()
    return composed
