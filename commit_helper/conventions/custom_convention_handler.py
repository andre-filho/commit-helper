# custom commits are only acceptable when you have a config file
from commit_helper.utils.text_utils import debug
from commit_helper.utils.text_utils import get_context


def custom_convention(tag, message, config_file, debug_mode):
    debug('tag', tag, debug_mode)
    debug('message', message, debug_mode)
    debug('pattern from file', config_file['commit_pattern'], debug_mode)

    pattern = str(config_file['commit_pattern'] or '')
    debug('pattern processed', pattern, debug_mode)

    context = ''

    pattern = pattern.replace('tag', str(tag))
    pattern = pattern.replace('message', str(message))
    debug('pattern post replace', pattern, debug_mode)

    if config_file['context']:
        context = get_context()
        pattern.replace('context', context)

    pattern += '\n'
    return pattern
