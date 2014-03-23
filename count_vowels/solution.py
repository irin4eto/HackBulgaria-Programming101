def count_vowels(str):
    count = 0
    for i in list(str.lower()):
        if i in 'aoueyi':
            count += 1
    return count
