import os

tag_type = int(input("""
what type of commit convention are you using?

1- angular
2- changelog
"""))

tag = str(input("type the tag: "))
msg = str(input("type the commit message: ")).lower()

commit_msg_pre = 'git commit -m '

if tag_type == 1:
    context = str(input('type the context: ')).lower()
    tag = tag.lower()
    composed_msg = commit_msg_pre + "'" + tag + "(" + context + ")" +": " + msg + "'"
    # os.system(composed_msg)
    os.system("git commit -m '%s(%s): %s'" % (tag, context, msg))
else:
    composed_msg = commit_msg_pre + "'" + tag.upper() + ": " + msg + "'"
    os.system(composed_msg)
