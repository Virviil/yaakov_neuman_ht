from my_log import LOG

_MY_WORDS = {}


def set_words(js: dict):
    if js:
        words = js.get('words')
        if words:
            word_list = words.split(',')
            # Update the words in _MY_WORDS:
            for word in word_list:
                if word in _MY_WORDS:
                    LOG.debug(f'Update word: {word}')
                    _MY_WORDS[word] += 1
                else:
                    LOG.info(f'Add new word: {word}')
                    _MY_WORDS[word] = 1
    # Returns 204 NO CONTENT
    return '', 204


def frequency_distribution_rank(count: int, low: int, high: int):
    return round(4 * (count - low) / (high - low) + 1)


def get_words_stat():
    values = {count for _, count in _MY_WORDS.items()}
    low = min(values)
    high = max(values)

    stat = {word: frequency_distribution_rank(count, low, high) for word, count in _MY_WORDS.items()}
    return stat
