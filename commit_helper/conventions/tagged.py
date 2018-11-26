def tagged_convention(tag, msg):
    tag = tag.upper()
    composed_message = "%s: %s\n" % (tag, msg)
    return composed_message


tagged_convention_help = \
    """
    Convention format:

    TAG: message
    ---
    Tag usage:

    ADD:


    """
