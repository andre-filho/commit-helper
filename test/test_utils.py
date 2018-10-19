import utils
# import yaml


def test_get_text():
    inputs = [
        "tag",
        "message",
    ]

    def mock_input(s):
        return inputs.pop(0)

    utils.input = mock_input
    a, b = utils.get_text()
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
    utils.input = mock_input
    a = utils.get_context()
    if not a == 'context':
        raise AssertionError()


def test_sanitize_as_empty_string():
    string = 'asopdfha'
    string2 = None
    string = utils.sanitize_as_empty_string(string)
    string2 = utils.sanitize_as_empty_string(string2)
    if not (string == 'asopdfha' and string2 == ''):
        raise AssertionError()


def test_gen_co_author():
    arg = utils.gen_co_author('kiryto <black.swordsman@aincrad.com>')
    if not arg == "\nCo-authored-by: kiryto <black.swordsman@aincrad.com>":
        raise AssertionError()

    arg2 = utils.gen_co_author('')
    if not arg2 == '':
        raise AssertionError()


def test_debug(capsys):
    utils.debug('msg', 666, show=True)
    captured = capsys.readouterr()
    if not captured.out == "DEBUG-> msg: 666\n":
        raise AssertionError()

# FIXME
# def test_create_file(tmpdir):
#     test_file = tmpdir.mkdir('test').join('commiter.yml')
#     utils.create_file("changelog")
#     stream = open('commiter.yml', 'r')
#     convention = yaml.load(stream)
#     if not convention['convention'] == 'changelog':
#         raise AssertionError()
