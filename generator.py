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
from utils import menu
from utils import parser_cli
from utils import create_file


parser = parser_cli()
args = parser.parse_args()

file_path = Path('commiter.yml')
if file_path.is_file():
    with open(str(file_path), 'r') as stream:
        try:
            config = safe_load(stream)
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
else:
    print("No config files found!\nRunning default script...")
    opt = int(input(menu) or 4)
    if opt == 1:
        print("You're using the angular convention")
        angular_convention(parser.co_author)
        create_file('angular')
    elif opt == 2:
        print("You're using the changelog convention")
        changelog_convention(args.co_author)
        create_file('changelog')
    elif opt == 3:
        print("You're using the symphony convention")
        symphony_convention(args.co_author)
        create_file('symphony')
    elif opt == 4:
        print("You're not using a convention")
        just_message(args.co_author)
        create_file('none')
