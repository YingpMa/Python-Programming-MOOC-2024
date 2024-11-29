# Write your solution here
def shortest(my_list: list):
    length = len(my_list[0])
    result = my_list[0]
    for item in my_list:
        if length > len(item):
            result = item
            length = len(item)
    return result