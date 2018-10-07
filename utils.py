import argparse
from yaml import dump

supported_conventions = [
    "angular",
    "changelog",
    "symphony",
    "message",
]

menu = """
    What type of commit convention are you using?

    default: Just the message
    1: Karma/Angular
    2: Conventional changelog
    3: Symfony CMF

    """


def get_text(context=False):
    if context:
        tag = str(input("type the tag: "))
        msg = str(input("type the commit message: ")).lower()
        context = str(input('type the context: ')).lower()
        return tag, msg, context
    else:
        tag = str(input("type the tag: "))
        msg = str(input("type the commit message: ")).lower()
        return tag, msg


def create_file(convention_name, dont_create=False):
    if not dont_create:
        data = dict(
            convention=convention_name
        )
        with open('commiter.yml', 'w') as output_file:
            dump(data, output_file, default_flow_style=False)


def parser_cli():
    desc = "A commit formatter tool to help you follow commit conventions."
    help_convention = \
        """
        Selects a convention to be used for the commit.
        Required if there's no commiter.yml file.
        """
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("--co-author",
                        help="make your friend an co-author to the commit",
                        dest="co_author", default=None)
    parser.add_argument("--no-generate", dest="no_file",
                        help="disables the creation of a commiter.yml file",
                        default=True, type=bool)
    parser.add_argument("--convention", choices=supported_conventions,
                        dest="convention", default='', help=help_convention)
    return parser


def change_if_none(string):
    if string is None:
        return ''
    return string
