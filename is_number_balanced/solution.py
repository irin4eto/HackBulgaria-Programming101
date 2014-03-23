def is_number_balanced(n):
    arr_str = list(str(n))
    left_side = 0
    right_side = 0
    arr_int = list(map(int, arr_str))
    if len(arr_int) <= 1:
        return True
    for i in range(len(arr_int) // 2):
        left_side += arr_int[i]
    if len(arr_int) % 2 != 0:
        for i in range(len(arr_int) // 2 + 1, len(arr_int)):
            right_side += arr_int[i]
    else:
        for i in range(len(arr_int) // 2, len(arr_int)):
            right_side += arr_int[i]
    return left_side == right_side
