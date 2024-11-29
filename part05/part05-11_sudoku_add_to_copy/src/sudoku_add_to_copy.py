# Write your solution here
def print_sudoku(sudoku: list):
    for i in range(9):
        for j in range(9):
            if j in [0, 1, 3, 4, 6, 7 ]:
                if sudoku[i][j] == 0:
                    print("_ ", end="")
                else:
                    print(f"{sudoku[i][j]} ", end="")
            if j in [2, 5]:
                if sudoku[i][j] == 0:
                    print("_  ", end="")
                else:
                    print(f"{sudoku[i][j]}  ", end ="")
            if j == 8:
                if sudoku[i][j] == 0:
                    print("_")
                else:
                    print(f"{sudoku[i][j]}")                

        if i in [2, 5]:
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = []
    list_value = []
    for item in sudoku:
        list_value = []
        for i in item:
            list_value.append(i)
        new_sudoku.append(list_value)
         
    new_sudoku[row_no][column_no] = number
    return new_sudoku

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)    
