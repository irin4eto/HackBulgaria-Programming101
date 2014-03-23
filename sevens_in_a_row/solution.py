def sevens_in_a_row(arr, n):
    count = 1
    i = 0;
    len_arr = len(arr) - 1
    while i < len_arr:
        if arr[i] == 7:
            while arr[i] == arr[i + 1]:
                count = count + 1
                i = i + 1
                if i >= len_arr:
                    break
            if count == n:
                return True
            else:
                count = 1
        i = i + 1
    return False
