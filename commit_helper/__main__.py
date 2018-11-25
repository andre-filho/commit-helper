# dependencies imports
from pathlib import Path
# utils imports
from .utils.utils import parser_cli
from .utils.text_utils import debug
from .utils.file_handler import handle_file_based_commit
from .utils.flag_commit_handler import convention_flag_handler
from .conventions.convention_help_handler import convention_help_handler


def main():
    parser = parser_cli()
    args = parser.parse_args()
    debug_mode = args.debug

    debug('args variable', args, debug_mode)

    file_path = Path('commiter.yml')

    debug('file_path', file_path, debug_mode)

    if args.show_convention_tags is not '':
        convention_help_handler(file_path, args, debug_mode)
        return

    elif args.convention is not '':
        convention_flag_handler(args, debug_mode)
        return

    elif file_path.is_file():
        handle_file_based_commit(file_path, debug_mode, args)
        return

    else:
        debug('parser full return', parser.parse_args(), debug_mode)
        parser.print_help()
