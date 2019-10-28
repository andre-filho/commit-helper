import re


class ConventionedCommit:
    """
    Class for normal commits, following the most basic good practices.
    Validates if it contains 50 > characters.

    E.x: Adds docstring to ConventionedCommit class
    """

    help_text = ''
    regex = r'.{1,50}'

    def validate(self, message) -> bool:
        """
        Validates the formatted commit with the convention's standards
        """
        pass

    def format(self) -> None:
        """
        Formats all the commit pieces into the convention
        """

        pass

    def generate_configuration_file(self) -> None:
        """
        Generates the configuration file for that convention
        """
        pass

    def show_help(self) -> None:
        """
        Prints the convention's help guide on screen
        """
        pass

    def get_message(self) -> str:
        """
        Get user's input for message
        """
        pass

    def write_commit(self) -> None:
        """
        Writes the commit into the commit tree
        """
        pass


class TaggedConventionedCommit(ConventionedCommit):
    """

    """
    valid_tags = [
        'ADD',
        'CHR',
        'DEL',
        'REF',
        '',
        '',
    ]

    def __init__(self):
        listt = []

        for tag in valid_tags:
            listt.append('^%s$' % tag)

        self.regex = r'[%s]' % str.join(listt)


class CustomConventionedCommit(ConventionedCommit):
    """
    """
    regex = r''
    pass
