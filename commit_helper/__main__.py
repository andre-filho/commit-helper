from pathlib import Path

from .utils.utils import parser_cli
from .utils.text_utils import debug
from .utils.file_handler import handle_file_based_commit
from .utils.file_handler import get_file_path
from .utils.flag_commit_handler import convention_flag_handler

from .conventions.convention_help_handler import convention_help_handler


class CommitHelper:
    __instance = None

    def __init__(self):
        """Private constructor for CommitHelper singleton class facade"""
        if CommitHelper.__instance != None:
            raise Exception("Singletons are supposed to be single instances!")
        else:
            CommitHelper.__instance = self

    @staticmethod
    def get_instance() -> CommitHelper():
        """Returns singleton for class"""
        if CommitHelper.__instance == None:
            CommitHelper()
        return CommitHelper.__instance

    @staticmethod
    def create_commit() -> None:
        pass

    @staticmethod
    def configure_convention() -> None:
        pass

    @staticmethod
    def show_convention_help() -> None:
        pass


def main():
    """
    Main function. Called by CLI.
    """
    parser = parser_cli()
    args = parser.parse_args()
    debug_mode = args.debug

    debug('args variable', args, debug_mode)

    file_path = get_file_path()

    debug('file_path', file_path, debug_mode)

    if args.show_convention_tags is True:
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
