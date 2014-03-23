def is_prime(number):
    return abs(number) != 1 and not len([x for x in range(2, int(abs(number ** 0.5)) + 1) if number % x == 0])

def goldbach(n):
    result = []
    all_prime = [x for x in range(n) if is_prime(x)]
    for i in range(len(all_prime)):
        for j in range(i, len(all_prime)):
            if all_prime[i] + all_prime[j] == n:
                result.append((all_prime[i], all_prime[j]))
    return result
