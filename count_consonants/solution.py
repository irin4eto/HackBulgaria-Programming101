def count_consonants(str):
    count = 0
    for i in list(str.lower()):
        if i in 'bcdfghjklmnpqrstvwxz':
            count = count + 1
    return count
