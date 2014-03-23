def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    if n == 2:
        return listB
    if n == 3:
        return listA + listB
    return nth_fib_lists(listB, listA + listB, n - 1)
