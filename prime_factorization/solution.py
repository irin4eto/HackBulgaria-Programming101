def is_prime(number):
    return abs(number) != 1 and not len([x for x in range(2, int(abs(number ** 0.5)) + 1) if number % x == 0])

def prime_factorization(number):
    devisors = {}
    devisor = 2
    while number != 0 and devisor <= number:
        if number % devisor == 0 and is_prime(devisor):
            if devisor in devisors.keys():
                devisors[devisor] += 1
            else:
                devisors[devisor] = 1
            number /= devisor
            while number != 0 and number % devisor == 0:
                if devisor in devisors.keys():
                    devisors[devisor] += 1
                else:
                    devisors[devisor] = 1
                number /= devisor
        devisor += 1
    return sorted(list(devisors.items()))
