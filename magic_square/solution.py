def magic_square(matrix):
    matrix_list = []
    result = []
    sum_roww = 0
    sum_coll = 0
    sum_diag = 0

    for i in range(len(matrix)):
        matrix_list = matrix_list + matrix[i]

    for i in range(0, len(matrix_list) - 2, len(matrix[0])):
        for j in range(i, i + len(matrix[0])):
            sum_roww = sum_roww + matrix_list[j]
        result.append(sum_roww)
        sum_roww = 0


    for i in range(0, len(matrix[0])):
        for j in range(i, len(matrix_list), len(matrix[0])):
            sum_coll = sum_coll + matrix_list[j]
        result.append(sum_coll)
        sum_coll = 0

    for i in range(0, len(matrix_list), 4):
        sum_diag = sum_diag + matrix_list[i]
    result.append(sum_diag)
    sum_diag = 0

    for i in range(len(matrix[0]) - 1, len(matrix_list) - 2, len(matrix[0]) - 1):
        sum_diag = sum_diag + matrix_list[i]
    result.append(sum_diag)

    if len(set(result)) == 1:
        return True
    else:
        return False
