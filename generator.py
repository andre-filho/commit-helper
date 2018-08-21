import os

tag_type = int(input("""
what type of commit convention are you using?

1- angular
2- changelog
"""))

tag = str(input("type the tag: "))
msg = str(input("type the commit message: ")).lower()

if tag_type == 1:
    context = str(input('type the context: ')).lower()
    tag = tag.lower()
    os.system("git commit -m '%s(%s): %s'" % (tag, context, msg))
else:
    tag.upper()
    os.system("git commit -m '%s: %s'" % (tag, msg))
