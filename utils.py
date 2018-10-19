import argparse
from yaml import dump

supported_conventions = [
    "angular",
    "karma",
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


def get_text():
    tag = str(input("type the tag: "))
    msg = str(input("type the commit message: ")).lower()
    return tag, msg


def get_context():
        context = str(input('type the context: ') or '').lower()
        return context


def gen_co_author(co_author):
    if co_author is '':
        return ''
    return "\nCo-authored-by: %s" % co_author


def create_file(convention_name, dont_create=False): # pragma: no cover
    if not dont_create:
        data = dict(
            convention=convention_name
        )
        with open('commiter.yml', 'w') as output_file:
            dump(data, output_file, default_flow_style=False)
        print('Successfully created the commiter file.')


def parser_cli():
    desc = "A commit formatter tool to help you follow commit conventions."
    help_convention = \
        """
        Selects a convention to be used for the commit.
        Required if there's no commiter.yml file.
        """
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-ca", "--co-author",
                        help="Make your friend an co-author to the commit",
                        dest="co_author", default='')
    parser.add_argument("-nf", "--no-file", dest="no_file",
                        help="Disables the creation of a commiter.yml file",
                        action="store_true")
    parser.add_argument("-c", "--convention", choices=supported_conventions,
                        dest="convention", default='', help=help_convention)
    parser.add_argument("-d", "--debug", action="store_true", dest="debug",
                        help="Toggles debug option")
    return parser


def sanitize_as_empty_string(string):
    if string is None:
        return ''
    return string


def debug(message, value, show=False):
    if show:
        print("DEBUG-> %s: %s" % (message, value))
