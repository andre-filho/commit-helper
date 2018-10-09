#! /usr/bin/env python3

# dependencies imports
from pathlib import Path
from yaml import safe_load
from yaml import YAMLError

# conventions imports
from conventions.karma_angular import angular_convention
from conventions.changelog import changelog_convention
from conventions.symphony_cmf import symphony_convention
from conventions.no_convention import just_message

# utils imports
from utils import parser_cli
from utils import create_file
from utils import debug


def main(debug_mode=False):
    file_path = Path('commiter.yml')
    debug('file_path', file_path, debug_mode)
    if file_path.is_file():
        with open(str(file_path), 'r') as stream:
            try:
                config = safe_load(stream)
                debug('convention from file', config['convention'], debug_mode)
                if config['convention'] is not None:
                    convention = str(config['convention']).lower()
                else:
                    convention = 'none'
                if convention == 'angular' or convention == 'karma':
                    print('You are using the %s convention' % convention)
                    angular_convention(args.co_author)
                elif convention == 'changelog':
                    print('You are using the %s convention' % convention)
                    changelog_convention(args.co_author)
                elif convention == 'symphony':
                    print('You are using the %s convention' % convention)
                    symphony_convention(args.co_author)
                elif convention == 'none':
                    just_message(args.co_author)
            except YAMLError as exc:
                print(exc)

    elif args.convention is not '':
        convention = str(args.convention)
        debug('convention flag', convention, debug_mode)
        if convention == 'angular' or convention == 'karma':
            angular_convention(args.co_author)
            create_file(convention, args.no_file)
        elif convention == 'changelog':
            changelog_convention(args.co_author)
            create_file(convention, args.no_file)
        elif convention == 'symphony':
            symphony_convention(args.co_author)
            create_file(convention, args.no_file)
        elif convention == 'message':
            just_message(convention)
            create_file('none', args.no_file)

    else:
        debug('parser full return', parser.parse_args(), debug_mode)
        parser.print_help()


debug_option = False
parser = parser_cli()
args = parser.parse_args()
debug('args variable', args, debug_option)
main(debug_option)
