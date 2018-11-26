import yaml
import commit_helper.conventions.atom as atom
import commit_helper.conventions.tagged as tagged
import commit_helper.conventions.karma_angular as angular
import commit_helper.conventions.symphony_cmf as symphony
import commit_helper.conventions.custom_convention as custom
import commit_helper.conventions.no_convention as no_convention


def test_karma_angular_convention_with_context():
    message = angular.karma_angular_convention('TAG', 'message', 'context')
    if not (message == 'tag(context): message\n'):
        raise AssertionError()


def test_karma_angular_convention_without_context():
    message = angular.karma_angular_convention('tag', 'message', '')
    if not (message == 'tag: message\n'):
        raise AssertionError()


def test_tagged_convention():
    message = tagged.tagged_convention('tag', 'message')
    if not (message == 'TAG: message\n'):
        raise AssertionError()


def test_symphony_convention():
    message = symphony.symphony_convention('tag', 'message')
    if not (message == '[Tag] message\n'):
        raise AssertionError()


def test_custom_convention():
    fyle = yaml.safe_load("""
    convention: custom
    commit_pattern: tag..:..message
    context: false
    """)

    msg = "a nice function"
    tag = "add"
    message = custom.custom_convention(tag, msg, fyle, True)
    if not message == "add..:..a nice function\n":
        raise AssertionError()


def test_no_convention_without_args():
    inputs = [
        "message",
    ]

    def mock_input(s):
        return inputs.pop(0)

    no_convention.input = mock_input
    message = no_convention.just_message()
    if not message == 'Message\n':
        raise AssertionError()


def test_no_convention_with_args():
    message = no_convention.just_message('Message')
    if not message == 'Message\n':
        raise AssertionError()


def test_atom_convention():
    message = atom.atom_convention('CaNary', 'STUFF')
    if not message == ":canary: Stuff\n":
        raise AssertionError()
