from os import system
# utils imports
from .text_utils import debug
from .utils import create_file
from .utils import gen_co_author
from .utils import handle_conventioned_commit
# conventions imports
from commit_helper.conventions.no_convention import just_message


def convention_flag_handler(args, debug_mode):
    convention = str(args.convention)
    debug('convention flag', convention, debug_mode)

    if convention == 'message':
        if args.message is not '':
            commit_message = just_message(msg=args.message)
        else:
            commit_message = just_message()
        convention = 'none'

    else:
        commit_message = handle_conventioned_commit(convention, args)

    create_file(convention, args.no_file)
    commit_message += gen_co_author(args.co_author)
    debug('commit message', commit_message, debug_mode)
    system('git commit -m "%s"' % commit_message)
