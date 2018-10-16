#! /usr/bin/env python3

# dependencies imports
from pathlib import Path
from yaml import safe_load
from yaml import YAMLError
from os import system

# conventions imports
from conventions.karma_angular import angular_convention
from conventions.changelog import changelog_convention
from conventions.symphony_cmf import symphony_convention
from conventions.no_convention import just_message

# utils imports
from utils import parser_cli
from utils import create_file
from utils import debug
from utils import get_text
from utils import get_context
from utils import gen_co_author


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

                if convention == 'none':
                    commit_message = just_message()
                
                else:
                    tag, msg = get_text()
                    if convention == 'angular' or convention == 'karma':
                        print('You are using the %s convention' % convention)
                        context = get_context()
                        commit_message = angular_convention(tag,msg,context)
                    elif convention == 'changelog':
                        print('You are using the %s convention' % convention)
                        commit_message = changelog_convention(tag,msg)
                    elif convention == 'symphony':
                        print('You are using the %s convention' % convention)
                        commit_message = symphony_convention(tag,msg)
                
                commit_message += gen_co_author(args.co_author)
                debug('commit message', commit_message, debug_mode)
                system('git commit -m "%s"' % commit_message)

            except YAMLError as exc:
                print(exc)

    elif args.convention is not '':
        convention = str(args.convention)
        debug('convention flag', convention, debug_mode)

        
        if convention == 'message':
            commit_message = just_message()
            create_file('none', args.no_file)
        
        else:
            tag, msg = get_text()
            
            if convention == 'angular' or convention == 'karma':
                context = get_context()
                commit_message = angular_convention(tag,msg,context)
                create_file(convention, args.no_file)
            elif convention == 'changelog':
                commit_message = changelog_convention(tag,msg)
                create_file(convention, args.no_file)
            elif convention == 'symphony':
                commit_message = symphony_convention(tag,msg)
                create_file(convention, args.no_file)

        
        commit_message += gen_co_author(args.co_author)
        debug('commit message', commit_message, debug_mode)
        system('git commit -m "%s"' % commit_message)

    else:
        debug('parser full return', parser.parse_args(), debug_mode)
        parser.print_help()


parser = parser_cli()
args = parser.parse_args()
debug('args variable', args, args.debug)
main(args.debug)
