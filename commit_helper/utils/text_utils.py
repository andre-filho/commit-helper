def get_text():
    tag = str(input("type the tag: "))
    msg = str(input("type the commit message: ")).lower()
    return tag, msg


def get_context():
    context = str(input('type the context: ') or '').lower()
    return context


def sanitize_as_empty_string(string):
    if string is None:
        return ''
    return string


def debug(message, value, show=False):
    if show:
        print("DEBUG-> %s: %s" % (message, value))
