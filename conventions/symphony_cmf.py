from os import system


def symphony_convention(tag,msg):
    tag = tag.capitalize()
    composed = "[%s] %s\n" % (tag, msg)
