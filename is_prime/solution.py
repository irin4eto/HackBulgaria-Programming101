def is_prime(number):
    return abs(number) != 1 and not len([x for x in range(2, int(abs(number ** 0.5)) + 1) if number % x == 0])
