# dependencies imports
from yaml import safe_load
from yaml import YAMLError
# convention imports
from .atom import atom_convention_help
from .tagged import tagged_convention_help
from .karma_angular import karma_convention_help
from .karma_angular import angular_convention_help
from .symphony_cmf import symphony_convention_help
# utils imports
from commit_helper.utils.colors import HELP
from commit_helper.utils.colors import RESET
from commit_helper.utils.colors import MIN_ERROR
from commit_helper.utils.text_utils import debug
from commit_helper.utils.text_utils import print_help
from commit_helper.utils.utils import dump_convention


# TODO: test
def convention_help_handler(file_path, args, debug_mode):
    if file_path.is_file() and args.convention is '':
        debug('Found file', str(file_path), debug_mode)
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

    get_help_to_defined_convention(convention)


# TODO: test
def get_help_to_defined_convention(convention):
    if convention is 'angular':
        print_help(angular_convention_help)

    elif convention is 'tagged':
        print_help(tagged_convention_help)

    elif convention is 'karma':
        print_help(karma_convention_help)

    elif convention is 'symphony':
        print_help(symphony_convention_help)

    elif convention is 'atom':
        print_help(atom_convention_help)

    else:
        print(MIN_ERROR + 'The chosen convention has no helper!' + RESET)
