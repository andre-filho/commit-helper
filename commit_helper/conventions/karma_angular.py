def angular_convention(tag, msg, context):
    tag = tag.lower()
    if context == '':
        composed_message = "%s: %s\n" % (tag, msg)
    else:
        composed_message = "%s(%s): %s\n" % (tag, context, msg)
    return composed_message
