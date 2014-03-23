def is_prime(number):
    return abs(number) != 1 and not len([x for x in range(2, int(abs(number ** 0.5)) + 1) if number % x == 0])


def prime_number_of_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return is_prime(count)
