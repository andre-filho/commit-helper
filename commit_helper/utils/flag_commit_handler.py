from os import system
# utils imports
from .utils import create_file
from .utils import gen_co_author
from .utils import handle_conventioned_commit
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
        if args.message is not '':
            commit_message = just_message(msg=args.message)
        else:
            commit_message = just_message()

        create_file('none', args.no_file)

    else:
        commit_message = handle_conventioned_commit(convention, args)

    create_file(convention, args.no_file)
    commit_message += gen_co_author(args.co_author)
    debug('commit message', commit_message, debug_mode)
    system('git commit -m "%s"' % commit_message)
