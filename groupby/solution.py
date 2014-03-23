def groupby(func, seq):
    d = {}
    repeat_key = list(map(func, seq))
    key_set = set(repeat_key)
    key_list = list(key_set)

    for i in range(len(key_list)):
        d[key_list[i]] = []

    for i in range(0, len(key_list)):
        for j in range(0, len(repeat_key)):
            if repeat_key[j] == key_list[i]:
                d[key_list[i]].append(seq[j])

    return d
