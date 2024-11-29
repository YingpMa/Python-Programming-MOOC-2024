# Write your solution here
def formatted(my_list: list):
    new_list = []
    for item in my_list:
        new_list.append(f"{item:.2f}")
    return new_list

