def is_an_bn(word):
    if word == "":
        return True
    a_and_b = word.split('ab')
    b_and_a = word.split('ba')

    return len(a_and_b) == 2 and len(b_and_a) == 1 and \
        len(a_and_b[0]) == len(a_and_b[1])
