from collections import defaultdict

def unique_words_count(words):
    dict_words = defaultdict(str)
    dict_words = {x: 0 for x in words}
    return len(dict_words.keys())
