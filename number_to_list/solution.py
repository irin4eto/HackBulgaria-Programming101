def number_to_list(n):
    if n < 10:
        return [n]
    else:
        return number_to_list(n // 10) + [n % 10]
