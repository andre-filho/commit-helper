# dependencies imports
from pathlib import Path
# utils imports
from .utils.utils import parser_cli
from .utils.text_utils import debug
from .utils.file_handler import handle_file_based_commit
from .utils.flag_commit_handler import convention_flag_handler


def main():
    parser = parser_cli()
    args = parser.parse_args()
    debug_mode = args.debug
    debug('args variable', args, debug_mode)
    file_path = Path('commiter.yml')
    debug('file_path', file_path, debug_mode)
    if file_path.is_file():
        handle_file_based_commit(file_path, debug_mode, args)

    elif args.convention is not '':
        convention_flag_handler(args, debug_mode)

    else:
        debug('parser full return', parser.parse_args(), debug_mode)
        parser.print_help()
