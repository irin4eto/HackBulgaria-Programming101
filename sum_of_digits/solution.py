def sum_of_digits(n):
    return sum([int(x) for x in list(str(abs(n)))])
