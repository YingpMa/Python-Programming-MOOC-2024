# Write your solution here
def no_shouting(my_list: list):
    new_list = []
    for item in my_list:
        if not item.isupper():
            new_list.append(item)
    return new_list


if __name__ == "__main__":
    list1 = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(list1)
    print(pruned_list)