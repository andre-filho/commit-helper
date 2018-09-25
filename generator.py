from pathlib import Path
from yaml import safe_load
from yaml import YAMLError

from utils import run_config
from utils import angular_convention
from utils import changelog_convention
from utils import symphony_convention
from utils import just_message

tag = ''
tag_is_lowercase = False
tag_is_uppercase = False
tag_is_capitalized = False
convention = ''

file_path = Path("commiter.yml")

if file_path.is_file():
    with open(str(file_path), 'r') as stream:
        try:
            config = safe_load(stream)
            tag, tag_is_capitalized, tag_is_lowercase, tag_is_uppercase, convention = run_config(config, tag, tag_is_capitalized, tag_is_lowercase, tag_is_uppercase, convention)
            if convention != '' or convention != 'custom':
                if convention == 'angular':
                    print('You are using the %s convention' % convention)
                    angular_convention()
                elif convention ==  'changelog':
                    print('You are using the %s convention' % convention)
                    changelog_convention()
                elif convention == 'symphony':
                    print('You are using the %s convention' % convention)
                    symphony_convention()
                elif convention == 'none':
                    just_message()
            else:
                custom_convention()
        except YAMLError as exc:
            print(exc)

else:
    print("No config files found!\nRunning default script...")
    opt = int(raw_input("""
    what type of commit convention are you using?

    default: Just the message
    1: Karma/Angular
    2: Conventional changelog
    3: Symfony CMF
    """) or 4)

    if opt == 1:
        angular_convention()
    elif opt == 2:
       changelog_convention()
    elif opt == 3:
        symphony_convention()
    elif opt == 4:
        just_message()
