def sudoku_solved(sudoku):
    set_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    list_columns = []
    list_subgrids = []
    count_list_subgrids = -1

    for i in range(len(sudoku)):
        if set(sudoku[i]) != set_numbers:
            return False

    for i in range(len(sudoku)):
        list_columns.append([])
        for j in range(len(sudoku)):
            list_columns[i].append(sudoku[j][i])
    for i in range(len(list_columns)):
        if set(list_columns[i]) != set_numbers:
            return False

    for i in (range(len(sudoku))):
        list_subgrids.append([])

    for three_times in range(3):
        for count in range(3, len(sudoku) + 1, 3):
            count_list_subgrids += 1
            for i in range(count - 3, count):
                for j in range(count - 3, count):
                    list_subgrids[count_list_subgrids].append(sudoku[i][j])

    for i in range(len(list_subgrids)):
        if set(list_subgrids[i]) != set_numbers:
            return False

    return True


