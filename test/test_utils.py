import utils
# import yaml


def test_get_text_no_context():
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


def test_get_text_context():
    inputs = [
        "tag",
        "message",
        "context",
    ]

    def mock_input(s):
        return inputs.pop(0)
    utils.input = mock_input
    a, b, c = utils.get_text(context=True)
    if not a == 'tag':
        raise AssertionError()
    if not b == 'message':
        raise AssertionError()
    if not c == 'context':
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
    if not arg == "Co-authored-by: kiryto <black.swordsman@aincrad.com>":
        raise AssertionError()

    arg2 = utils.gen_co_author('')
    if not arg2 == '':
        raise AssertionError()

# FIXME
# def test_create_file(tmpdir):
#     test_file = tmpdir.mkdir('test').join('commiter.yml')
#     utils.create_file("changelog")
#     stream = open('commiter.yml', 'r')
#     convention = yaml.load(stream)
#     if not convention['convention'] == 'changelog':
#         raise AssertionError()
