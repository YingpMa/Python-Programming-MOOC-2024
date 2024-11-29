# Write your solution here
def most_common_character(string: str):
    times = 0
    list1 = []
    for item in string:
        if times < string.count(item):
            times = string.count(item)
    for item in string:
        if string.count(item) == times:
            list1.append(item)
    return list1[0]

    