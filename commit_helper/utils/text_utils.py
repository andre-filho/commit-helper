from .colors import RESET
from .colors import DEBUG_COLOR
from .colors import INPUT_COLOR
from .colors import NOTIFY_COLOR
from .colors import HELP


def get_text():
    """
    Gets the input for both tag and message.
    """
    tag = str(input(INPUT_COLOR + 'type the tag: ' + RESET))
    msg = str(input(INPUT_COLOR + 'type the commit message: ' + RESET)).lower()
    return tag, msg


def get_context():
    """
    Gets the input for the commit context and formats it to lowercase.
    """
    context = str(input(INPUT_COLOR + 'type the context: ' + RESET) or '')
    context.lower()
    return context


def sanitize_as_empty_string(string):
    """
    Checks if arg is None and returns it as an empty string.
    """
    if string is None:
        return ''
    return string


def notify(message):
    """
    Colored formatted print for notifications.
    """
    print(NOTIFY_COLOR + str(message) + RESET)


def debug(message, value, show=False):
    """
    Colored formatted print for debugging.
    """
    if show:
        mid = 'DEBUG: ' + str(message) + ' ~> ' + str(value)
        print(DEBUG_COLOR + mid + RESET)


def print_help(message):
    """
    Colored formatted print for help menus.
    """
    print(HELP + str(message) + RESET)


def handle_tag_message_args(tag='', message=''):
    """
    Checks if args are empty strings, if so it calls the get_text function.
    """
    if tag + message is not '':
        return tag, message
    return get_text()


def handle_context_arg(context=''):
    """
    Checks if context is empty and if it is calls a input function to get the
    context.
    """
    if context is not '':
        return context
    return get_context()
