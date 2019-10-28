import re


def tagged_convention(tag, msg) -> str:
    """
    Formats the convention following the tag convention.

    The tagged convention:
    <TAG>: <message>
    """
    tag = tag.upper()
    composed_message = "%s: %s\n" % (tag, msg)
    return composed_message


def is_message_valid(msg) -> bool:
    """
    Validates the commit message.
    """

    valid_tags = [
        r'\bADD\b',
        r'\bFEAT\b',
        r'\bDEL\b',
        r'\bCHR\b',
        r'\bMERGE\b',
        r'\bDOCS\b',
        r'\bFIX\b',
        r'\bREF\b',
        r'\bSTYLE\b',
        r'\bTEST\b',
        r'\bCI\b',
    ]

    comp = ''
    comp = comp.join(valid_tags)

    regx = r'([%s]+: \w+.*)' % comp

    if re.fullmatch(regx, msg) is None:
        return False

    return True


tagged_convention_help = \
    """
    The tagged convention:

    TAG: message
    <BLANK>
    <body>
    <BLANK>
    <footer>

    ---
    Tag usage:

    ADD     -> use for new files or methods
    FEAT    -> for when adding a new feature
    DEL     -> use for excluded files or methods
    CHR     -> use for normal dev work and maintainance
    MERGE   -> use for signal merges
    DOCS    -> for documentation changes
    FIX     -> use for solving bugs or failures in file
    REF     -> use for when you rename a file
    STYLE   -> use for fixing stylesheet errors
    TEST    -> use for test files
    CI      -> for that commit that aims for fix a build
    """
