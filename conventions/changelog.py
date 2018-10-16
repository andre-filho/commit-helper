from os import system

def changelog_convention(tag,msg):
    tag = tag.upper()
    composed_message = "%s: %s\n" % (tag, msg)
    return composed_message
