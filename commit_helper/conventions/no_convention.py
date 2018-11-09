from commit_helper.utils.colors import INPUT_COLOR
from commit_helper.utils.colors import RESET


def just_message(msg=''):
    if msg is '':
        message = str(input(INPUT_COLOR + "commit message: " + RESET))
    else:
        message = msg

    composed = "%s\n" % message.capitalize()
    return composed
