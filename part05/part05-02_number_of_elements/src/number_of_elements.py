# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for item in my_matrix:
        for n in item:
            if element == n:
                count += 1
    return count
