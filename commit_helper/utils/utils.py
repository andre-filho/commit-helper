import sys
import argparse
from yaml import dump
from .text_utils import notify
from .text_utils import handle_context_arg
from .text_utils import handle_tag_message_args
from commit_helper.conventions.atom import atom_convention
from commit_helper.conventions.tagged import tagged_convention
from commit_helper.conventions.symphony_cmf import symphony_convention
from commit_helper.conventions.karma_angular import karma_angular_convention


supported_conventions = [
    "angular",
    "karma",
    "tagged",
    "symphony",
    "message",
    "atom",
]


def gen_co_author(co_author):
    """
    Formats the co-author for putting into the commit body if it is not an
    empty string.
    """
    if co_author is '':
        return ''
    return '\nCo-authored-by: %s' % co_author


# TEST
def create_file(convention_name, dont_create=False):    # pragma: no cover
    """
    Creates a commit-helper.yml file with the given convention.
    """
    if not dont_create:
        data = dict(
            convention=convention_name
        )
        with open('commit-helper.yml', 'w') as output_file:
            output_file.write(dump(data, stream=None,
                                   default_flow_style=False))
        notify('Successfully created the commiter file.')


def parser_cli():
    """
    Calls argparser's parser to handle the CLI arguments.
    """
    desc = 'A commit formatter tool to help you follow commit conventions.'
    help_convention = \
        """
        Selects a convention to be used for the commit.
        Required if there's no commiter.yml file.
        """
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-t', '--tag', dest='tag', default='',
                        help='Pass your commit tag directly')
    parser.add_argument('-m', '--message', dest='message', default='',
                        help='Pass your commit message directly')
    parser.add_argument('-ct', '--context', dest='context', default='',
                        help='Pass your commit context directly')
    parser.add_argument('-ca', '--co-author',
                        help='Make your friend a co-author for the commit',
                        dest='co_author', default='')
    parser.add_argument('-nf', '--no-file', dest='no_file',
                        help='Disables the creation of a commiter.yml file',
                        action='store_true')
    parser.add_argument('-c', '--convention', choices=supported_conventions,
                        dest='convention', default='', help=help_convention)
    parser.add_argument('-d', '--debug', action='store_true', dest='debug',
                        help='Toggles debug option')
    parser.add_argument('-s', '--show', dest='show_convention_tags',
                        default='False', action='store_true',
                        help='Shows the rules of a given convention')
    return parser


def dump_convention(config_file):
    """
    Gets the convention's name from file.
    """
    if config_file['convention'] is None:
        return 'none'
    return str(config_file['convention']).lower()


# this function forces the program to quit if commiter file is invalid
def validate_commiter_file(stream_file):    # pragma: no cover
    """
    Checks if commit-helper file with custom convention has the
    required fields.
    """
    if stream_file['commit_pattern'] is None or stream_file['context'] is None:
        print(
            "Error: Your commit-helper file lacks a commit_pattern or context!"
        )
        sys.exit(0)

# REFACT: use function dict to keep code clean


def handle_conventioned_commit(convention, args):
    """
    Handler for conventioned commits.
    """
    tag, message = handle_tag_message_args(args.tag, args.message)
    commit_message = ''

    create_commit = dict(
        {
            # 'angular': handle_karma_angular,
            # 'karma': handle_karma_angular,
            'tagged': tagged_convention,
            'symphony': symphony_convention,
            'atom': atom_convention
        })

    if convention == 'angular' or convention == 'karma':
        context = handle_context_arg(args.context)
        return karma_angular_convention(tag, message, context)

    commit_message = create_commit[convention](tag, message)

    # elif convention == 'tagged':
    #     commit_message = tagged_convention(tag, message)

    # elif convention == 'symphony':
    #     commit_message = symphony_convention(tag, message)

    # elif convention == 'atom':
    #     commit_message = atom_convention(tag, message)

    return commit_message
