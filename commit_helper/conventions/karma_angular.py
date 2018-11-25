def karma_angular_convention(tag, msg, context):
    tag = tag.lower()
    if context == '':
        composed_message = "%s: %s\n" % (tag, msg)
    else:
        composed_message = "%s(%s): %s\n" % (tag, context, msg)
    return composed_message


angular_convention_help = \
    """
    General format:

    <tag>(<scope>): <message>
    <BLANK>
    <body>
    <BLANK>
    <footer>

    ----
    Tags:
    build:      Changes that affect the build system or external dependencies
    ci:         Changes to our CI configuration files and scripts
    docs:       Documentation only changes
    feat:       A new feature
    fix:        A bug fix
    perf:       A code change that improves performance
    refactor:   A code change that neither fixes a bug nor adds a feature
    style:      Changes that do not affect the meaning of the code
    test:       Adding missing tests or correcting existing tests

    ---
    Optional fields:
    <scope> or <context>, <body> and <footer>
    """

karma_convention_help = \
    """
    General format:

    <tag>(<scope>): <message>
    <BLANK>
    <body>
    <BLANK>
    <footer>

    ---
    Tags:
    feat:       New feature for the user, not a new feature for build script
    fix:        Bug fix for the user, not a fix to a build script
    docs:       Changes to the documentation
    style:      Formatting, missing semi colons, etc; no production code change
    refactor:   Refactoring production code, eg. renaming a variable
    test:       Adding missing tests, refactoring tests; no product code change
    chore:      Updating grunt tasks etc; no production code change

    ---
    Optional fields:
    <scope> or <context>, <body> and <footer>
    """
