# Write your solution here
def length_of_longest(my_list: list):
    length = 0
    for item in my_list:
        if len(item) > length:
            length = len(item)
    return length