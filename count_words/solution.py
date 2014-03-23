from functools import reduce

def count_words(words):
    return reduce(lambda d, x: dict(d, ** {x: d.get(x, 0) + 1}), words, {})
