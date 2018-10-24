from os import system
# utils imports
from .utils import create_file
from .utils import gen_co_author
from .text_utils import debug
from .text_utils import get_text
from .text_utils import get_context
# conventions imports
from commit_helper.conventions.karma_angular import angular_convention
from commit_helper.conventions.changelog import changelog_convention
from commit_helper.conventions.symphony_cmf import symphony_convention
from commit_helper.conventions.no_convention import just_message


def convention_flag_handler(args, debug_mode):
    convention = str(args.convention)
    debug('convention flag', convention, debug_mode)

    if convention == 'message':
        commit_message = just_message()
        create_file('none', args.no_file)

    else:
        tag, msg = get_text()

        if convention == 'angular' or convention == 'karma':
            context = get_context()
            commit_message = angular_convention(tag, msg, context)
            create_file(convention, args.no_file)
        elif convention == 'changelog':
            commit_message = changelog_convention(tag, msg)
            create_file(convention, args.no_file)
        elif convention == 'symphony':
            commit_message = symphony_convention(tag, msg)
            create_file(convention, args.no_file)

    commit_message += gen_co_author(args.co_author)
    debug('commit message', commit_message, debug_mode)
    system('git commit -m "%s"' % commit_message)
