from yaml import safe_load
from yaml import YAMLError

from .atom import atom_convention_help
from .tagged import tagged_convention_help
from .karma_angular import karma_convention_help
from .karma_angular import angular_convention_help
from .symphony_cmf import symphony_convention_help

from commit_helper.utils.colors import RESET
from commit_helper.utils.colors import MIN_ERROR
from commit_helper.utils.text_utils import debug
from commit_helper.utils.text_utils import print_help
from commit_helper.utils.utils import dump_convention


# TODO: test
def convention_help_handler(file_path, args, debug_mode):
    """
    Handles the user's help request.
    """
    if file_path.is_file() and args.convention is '':
        debug('Found file for help', str(file_path), debug_mode)
        with open(str(file_path)) as target:
            try:
                config = safe_load(target)
                convention = dump_convention(config)
                debug('Convention captured', convention, debug_mode)
            except YAMLError as err:
                print(err)

    elif args.convention is not '':
        debug('Found convention in args', args, debug_mode)
        convention = args.convention

    else:
        print(MIN_ERROR + 'No convention was specified!' + RESET)
        return

    debug('convention captured for helper', convention, debug_mode)
    get_help_to_defined_convention(convention, debug_mode)


# TODO: test
def get_help_to_defined_convention(convention, debug_mode):
    """
    Prints the help menu to the base conventions.
    """
    debug('recieved convention for help catch', convention, debug_mode)
    if convention == 'angular':
        print_help(angular_convention_help)

    elif convention == 'tagged':
        print_help(tagged_convention_help)

    elif convention == 'karma':
        print_help(karma_convention_help)

    elif convention == 'symphony':
        print_help(symphony_convention_help)

    elif convention == 'atom':
        print_help(atom_convention_help)

    else:
        print(MIN_ERROR + 'The chosen convention has no helper!' + RESET)
