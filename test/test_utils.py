# dependencies imports
import yaml
# utils imports
import commit_helper.utils.utils as utils
import commit_helper.utils.text_utils as text_utils
# color imports
from commit_helper.utils.colors import HELP
from commit_helper.utils.colors import RESET
from commit_helper.utils.colors import DEBUG_COLOR
from commit_helper.utils.colors import NOTIFY_COLOR


def test_get_text():
    inputs = [
        "tag",
        "message",
    ]

    def mock_input(s):
        return inputs.pop(0)

    text_utils.input = mock_input
    a, b = text_utils.get_text()
    if not a == 'tag':
        raise AssertionError()
    if not b == 'message':
        raise AssertionError()


def test_get_context():
    inputs = [
        "context",
    ]

    def mock_input(s):
        return inputs.pop(0)
    text_utils.input = mock_input
    a = text_utils.get_context()
    if not a == 'context':
        raise AssertionError()


def test_sanitize_as_empty_string():
    string = 'asopdfha'
    string = text_utils.sanitize_as_empty_string(string)
    if not string == 'asopdfha':
        raise AssertionError()

    string2 = None
    string2 = text_utils.sanitize_as_empty_string(string2)
    if not string2 == '':
        raise AssertionError()


def test_gen_co_author():
    arg = utils.gen_co_author('kiryto <black.swordsman@aincrad.com>')
    if not arg == "\nCo-authored-by: kiryto <black.swordsman@aincrad.com>":
        raise AssertionError()

    arg2 = utils.gen_co_author('')
    if not arg2 == '':
        raise AssertionError()


def test_debug(capsys):
    text_utils.debug('msg', 666, show=True)
    captured = capsys.readouterr()
    if not captured.out == DEBUG_COLOR + "DEBUG: msg ~> 666" + RESET + "\n":
        raise AssertionError()


def test_no_debug(capsys):
    text_utils.debug('msg', 666, show=False)
    captured = capsys.readouterr()
    if captured.out is not '':
        raise AssertionError()


def test_dump_convention():
    not_good_conf = """
    convention:
    """

    good_conf = """
    convention: asdf
    """
    response1 = utils.dump_convention(yaml.safe_load(not_good_conf))
    response2 = utils.dump_convention(yaml.safe_load(good_conf))

    if not response1 == 'none':
        raise AssertionError()

    if not response2 == 'asdf':
        raise AssertionError()


def test_notify(capsys):
    text_utils.notify('msg')
    captured = capsys.readouterr()
    if not captured.out == NOTIFY_COLOR + "msg" + RESET + "\n":
        raise AssertionError()


def test_handle_tag_message_args_with_args():
    tag, msg = text_utils.handle_tag_message_args('tag', 'msg')

    if not (tag is 'tag' and msg is 'msg'):
        raise AssertionError()


def test_handle_tag_message_args_without_args():
    inputs = ['tag', 'msg']

    def mock_input(s):
        return inputs.pop(0)

    text_utils.input = mock_input
    tag, msg = text_utils.handle_tag_message_args()

    if not (tag == 'tag' and msg == 'msg'):
        raise AssertionError()


def test_handle_context_arg_with_args():
    context = text_utils.handle_context_arg('context')

    if context is not 'context':
        raise AssertionError()


def test_handle_context_arg_without_args():
    inputs = ['context']

    def mock_input(s):
        return inputs.pop(0)

    text_utils.input = mock_input
    context = text_utils.handle_context_arg()

    if not context == 'context':
        raise AssertionError()


def test_print_help(capsys):
    text_utils.print_help('msg')
    captured = capsys.readouterr()
    if not captured.out == HELP + "msg" + RESET + "\n":
        raise AssertionError()
