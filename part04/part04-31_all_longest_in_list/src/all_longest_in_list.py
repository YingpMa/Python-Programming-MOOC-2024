# Write your solution here
def all_the_longest(my_list: list):
    length = 0
    new_list = []
    for item in my_list:
        if length < len(item):
            length = len(item)
    for item in my_list:
        if length == len(item):
            new_list.append(item)
    return new_list