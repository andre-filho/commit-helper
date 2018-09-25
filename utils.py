import os

possible_configurations = [
    'tag',
    'tag_is_lowercase',
    'tag_is_uppercase',
    'tag_is_capitalized',
    'convention',
]

# refactor this function, surely there is a better way of writing this
def run_config(array, tag, tag_is_capitalized, tag_is_lowercase, tag_is_uppercase,convention):
    for conf in possible_configurations:
        if conf in array:
            if conf == 'tag':
                tag = str(array[conf])
            elif conf == 'tag_is_lowercase':
                tag_is_lowercase = bool(array[conf])
            elif conf == 'tag_is_uppercase':
                tag_is_uppercase = bool(array[conf])
            elif conf == 'tag_is_capitalized':
                tag_is_capitalized = bool(array[conf])
            elif conf == 'convention':
                convention = str(array[conf])
    return tag, tag_is_capitalized, tag_is_lowercase, tag_is_uppercase, convention

def get_text(context=False):
    if context:
        tag = str(input("type the tag: "))
        msg = str(input("type the commit message: ")).lower()
        context = str(input('type the context: ')).lower()
        return tag, msg, context
    else:
        tag = str(input("type the tag: "))
        msg = str(input("type the commit message: ")).lower()
        return tag, msg

def angular_convention():
    tag, msg, context = get_text(context=True)
    tag = tag.lower()
    os.system("git commit -m '%s(%s): %s'" % (tag, context, msg))

def changelog_convention():
    tag, msg = get_text()
    tag = tag.upper()
    os.system("git commit -m '%s: %s'" % (tag, msg))

def symphony_convention():
    tag, msg = get_text()
    tag = tag.capitalize()
    os.system("git commit -m '[%s] %s'" % (tag, msg))

def just_message():
    msg = str(input("commit message: "))
    os.system("git commit -m '%s'" % msg.capitalize())

# FUTURE: implement
def custom_convention():
    pass
