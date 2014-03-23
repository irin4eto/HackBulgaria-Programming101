def simplify_fraction(fractions):
    numerator = fractions[0]
    denumenator = fractions[1]
    min = numerator
    if denumenator < numerator:
        min = denumenator
    for i in range(2, min + 1):
        if numerator % i == 0 and denumenator % i == 0:
            while numerator % i == 0 and denumenator % i == 0:
                numerator = numerator / i
                denumenator = denumenator / i
    return (int(numerator), int(denumenator))
