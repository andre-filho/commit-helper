from .colors import RESET
from .colors import DEBUG_COLOR
from .colors import INPUT_COLOR
from .colors import NOTIFY_COLOR


def get_text():
    tag = str(input(INPUT_COLOR + 'type the tag: ' + RESET))
    msg = str(input(INPUT_COLOR + 'type the commit message: ' + RESET)).lower()
    return tag, msg


def get_context():
    context = str(input(INPUT_COLOR + 'type the context: ' + RESET) or '')
    context.lower()
    return context


def sanitize_as_empty_string(string):
    if string is None:
        return ''
    return string


def notify(message):
    print(NOTIFY_COLOR + str(message) + RESET)


def debug(message, value, show=False):
    if show:
        mid = 'DEBUG: ' + str(message) + ' ~> ' + str(value)
        print(DEBUG_COLOR + mid + RESET)


def handle_tag_message_args(tag='', message=''):
    if tag + message is not '':
        return tag, message
    return get_text()


def handle_context_arg(context=''):
    if context is not '':
        return context
    return get_context()
