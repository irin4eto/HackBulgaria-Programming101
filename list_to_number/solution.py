def list_to_number(digits):
    number = 0
    digit = 1
    digits.reverse()
    for i in range(len(digits)):
        number += digits[i] * digit
        digit *= 10
    return number
