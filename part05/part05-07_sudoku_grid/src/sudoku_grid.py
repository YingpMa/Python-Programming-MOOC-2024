# Write your solution here
def row_correct(sudoku: list, row_no: int):
    list1 = []
    for item in sudoku[row_no]:
        if item != 0:
            if item not in list1:
                list1.append(item)
            else:
                return False
    return True

# Write your solution here
def column_correct(sudoku: list, column_no: int):
    list1 = []
    for item in sudoku:
        if item[column_no] != 0:
            if item[column_no] not in list1:
                list1.append(item[column_no])
            else:
                return False
    return True

# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    new_list = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            value = sudoku[i][j]
            if value != 0:
                if value not in new_list:
                    new_list.append(value)
                else:
                    return False
    return True

def sudoku_grid_correct(sudoku: list):
    logic1 = True
    logic2 = True
    logic3 = True
    for i in range(len(sudoku)):
        logic1 = row_correct(sudoku, i)
        if logic1 == False:
            return False
    for j in range(len(sudoku)):
        logic2 = column_correct(sudoku, j)
        if logic2 == False:
            return False
    for m in [0, 3, 6]:
        for n in [0, 3, 6]:
            logic3 = block_correct(sudoku, m, n)
            if logic3 == False:
                return False
    return True

if __name__ == "__main__":
        sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]

        print(sudoku_grid_correct(sudoku1))

        sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
        ]

        print(sudoku_grid_correct(sudoku2))