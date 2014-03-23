def prepare_meal(number):
    result = ''
    while number % 3 == 0:
        result = result + ' spam'
        number = number // 3
    while number % 5 == 0:
        if result == '':
            result = ' eggs'
            number = number // 5
        else:
            result = result + ' and eggs'
            number = number // 5
    return result
