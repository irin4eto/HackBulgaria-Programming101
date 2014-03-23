def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    if n == 2:
        return listB
    if n == 3:
        return listA + listB
    return nth_fib_lists(listB, listA + listB, n - 1)

def is_equal_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    else:
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
    return True

def member_of_nth_fib_lists(listA, listB, needle):
    n = 1
    fib_lists = nth_fib_lists(listA, listB, n)
    while len(fib_lists) <= len(needle):
        if is_equal_lists(fib_lists, needle):
            return True
        n += 1
        fib_lists = nth_fib_lists(listA, listB, n)
    return False
