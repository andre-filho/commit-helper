def atom_convention(tag, msg):
    tag = tag.lower()
    msg = msg.capitalize()
    composed_message = ":%s: %s\n" % (tag, msg)
    return composed_message


atom_convention_help = \
    """
    The atom convention:

    :<tag>: <Message>
    <BREAK>
    <body>
    <BREAK>

    ---
    Tags:
    - art:               when improving the format/structure of the code
    - racehorse:         when improving performance
    - non-potable_water: when plugging memory leaks
    - memo:              when writing docs
    - penguin:           when fixing something on Linux
    - apple:             when fixing something on macOS
    - checkered_flag:    when fixing something on Windows
    - bug:               when fixing a bug
    - fire:              when removing code or files
    - green_heart:       when fixing the CI build
    - white_check_mark:  when adding tests
    - lock:              when dealing with security
    - arrow_up:          when upgrading dependencies
    - arrow_down:        when downgrading dependencies
    - shirt:             when removing linter warnings

    ---
    Message rules:
    - Use the present tense ("Add feature" not "Added feature")
    - Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
    """
