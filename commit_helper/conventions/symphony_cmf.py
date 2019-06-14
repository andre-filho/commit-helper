def symphony_convention(tag, msg):
    """
    Formats the commit following the symphony convention.

    The symphony CMF convention:
    [<Tag>] <message>
    """
    tag = tag.capitalize()
    composed = "[%s] %s\n" % (tag, msg)
    return composed


symphony_convention_help = \
    """
    The symphony CMF convention:

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
