import yaml
import commit_helper.conventions.karma_angular as angular
import commit_helper.conventions.changelog as changelog
import commit_helper.conventions.symphony_cmf as symphony
import commit_helper.conventions.no_convention as no_convention
import commit_helper.conventions.custom_convention_handler as custom


def test_angular_convention_with_context():
    message = angular.angular_convention('TAG', 'message', 'context')
    if not (message == 'tag(context): message\n'):
        raise AssertionError()


def test_angular_convention_without_context():
    message = angular.angular_convention('tag', 'message', '')
    if not (message == 'tag: message\n'):
        raise AssertionError()


def test_changelog_convention():
    message = changelog.changelog_convention('tag', 'message')
    if not (message == 'TAG: message\n'):
        raise AssertionError()


def test_symphony_convention():
    message = symphony.symphony_convention('tag', 'message')
    if not (message == '[Tag] message\n'):
        raise AssertionError()


def test_custom_convention_handler():
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


def test_no_convention():
    inputs = [
        "message",
    ]

    def mock_input(s):
        return inputs.pop(0)
    no_convention.input = mock_input
    message = no_convention.just_message()
    if not message == 'Message\n':
        raise AssertionError()
