from yaml import dump

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

def create_file(convention_name):
    data = dict(
        convention = convention_name
    )
    with open('commiter.yml', 'w') as output_file:
        dump(data, output_file, default_flow_style=False)
