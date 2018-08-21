import os

opt = int(input("""
what type of commit convention are you using?

1- Karma/Angular
2- Conventional changelog
3- Symfony CMF
"""))

tag = str(input("type the tag: "))
msg = str(input("type the commit message: ")).lower()

if opt == 1:
    context = str(input('type the context: ')).lower()
    tag = tag.lower()
    os.system("git commit -m '%s(%s): %s'" % (tag, context, msg))

elif opt == 2:
    tag = tag.upper()
    os.system("git commit -m '%s: %s'" % (tag, msg))

elif opt == 3:
    tag = tag.capitalize()
    os.system("git commit -m '[%s] %s'" % (tag, msg))
