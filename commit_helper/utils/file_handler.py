from os import system
from yaml import safe_load
from yaml import YAMLError
# utils imports
from .text_utils import debug
from .text_utils import notify
from .text_utils import get_text
from .utils import gen_co_author
from .utils import dump_convention
from .utils import validate_commiter_file
from .utils import handle_conventioned_commit
# conventions imports
from commit_helper.conventions.no_convention import just_message
from commit_helper.conventions.custom_convention import custom_convention


def handle_file_based_commit(file_path, debug_mode, args):
    with open(str(file_path), 'r') as stream:
        try:
            config = safe_load(stream)
            debug('convention from file', config['convention'], debug_mode)
            convention = dump_convention(config)

            if convention == 'none':
                notify('You are not using a convention')
                if args.message is not '':
                    commit_msg = just_message(msg=args.message)
                else:
                    commit_msg = just_message()

            elif convention == 'custom':
                notify('You are using your custom convention')
                validate_commiter_file(config)
                tag, msg = get_text()
                commit_msg = custom_convention(tag, msg, config, debug_mode)

            else:
                notify('You are using the %s convention' % convention)
                commit_msg = handle_conventioned_commit(convention, args)

            commit_msg += gen_co_author(args.co_author)
            debug('commit message', commit_msg, debug_mode)
            system('git commit -m "%s"' % commit_msg)

        except YAMLError as err:
            print(err)
