import yaml
import commit_helper.utils.utils as utils
import commit_helper.utils.text_utils as text_utils
# from commit_helper.utils.utils import validate_commiter_file
# import commit_helper.utils.file_handler as file_utils
# import commit_helper.utils.flag_commit_handler as flag_utils


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
    if not captured.out == "DEBUG-> msg: 666\n":
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
