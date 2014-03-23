def sort_fractions(fractions):
    divided = [x[0] / x[1] for x in fractions]
    comparison = {divided[i]: fractions[i] for i in range(len(fractions))}
    divided.sort()
    return [comparison[x] for x in divided]
