def symphony_convention(tag, msg):
    tag = tag.capitalize()
    composed = "[%s] %s\n" % (tag, msg)
    return composed


symphony_convention_help = \
    """
    General format:

    [<Tag>] <message>
    <BLANK>
    <body>
    <BLANK>
    <changes>
    <BLANK>
    <footer>

    ---
    Obs.:
    Tag is not a tag similar to other commit conventions, it is actually a
    context to what was changed.

    ---
    Optionals:
    <body>, <changes>, <footer>
    """
