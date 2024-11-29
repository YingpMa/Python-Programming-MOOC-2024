# Write your solution here
def transpose(matrix: list):
    new_matrix = []
    n = len(matrix)
    for i in range(n):
        list_m = []
        for j in range(n):
            list_m.append(matrix[j][i])
        new_matrix.append(list_m)
    matrix[:] = new_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(transpose(matrix))