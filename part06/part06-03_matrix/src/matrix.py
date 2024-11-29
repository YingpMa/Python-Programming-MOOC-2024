# write your solution here
def row_sums():
    with open("matrix.txt") as new_file:
        row_list =[]
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            parts_sum = 0
            for item in parts:
                parts_sum += int(item)
            row_list.append(parts_sum)
    return row_list        

def matrix_sum():
    with open("matrix.txt") as new_file:
        row_list = row_sums()
        results = 0
        for item in row_list:
            results += item
    return results

def matrix_max():
    with open("matrix.txt") as new_file:
        matrix_list = []
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            for item in parts:
                item = int(item)
                matrix_list.append(item)
        matrix_list.sort()

    return matrix_list[-1]

if __name__ == "__main__":
    print(row_sums())
    print(matrix_max())
    print(matrix_sum())
