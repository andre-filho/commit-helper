from os import system

def angular_convention(tag,msg,context):
    tag = tag.lower()
    if context is '':
        composed_message = "%s: %s\n" % (tag, msg)
    composed_message = "%s(%s): %s\n" % (tag, context, msg)
    return composed_message
