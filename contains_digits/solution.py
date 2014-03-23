def contains_digits(number, digits):
    if len(digits) == 0:
        return True
    else:
        store_all_digits = list(map(int, list(str(number))))
        return len(digits) == len(list(filter(lambda x: x in store_all_digits, digits)))
