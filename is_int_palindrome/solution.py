def is_int_palindrome(n):
    arr = list(str(n))
    index = 0
    len_arr = len(arr) - 1
    while index <= len_arr and arr[index] == arr[len_arr]:
        if len(arr) % 2 != 0 and index == len_arr:
            return True
        if len(arr) % 2 == 0 and index == len_arr - 1:
            return True
        index += 1
        len_arr -= 1
    return False
