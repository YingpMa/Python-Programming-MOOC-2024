# Write your solution here
def longest_series_of_neighbours(my_list: list):
    if not my_list:
        return 0
    longest = 1
    value = 1
    for i in range(1,len(my_list)):
        if abs(my_list[i] - my_list[i-1]) == 1:
            value += 1
            longest = max(value, longest)
        else:
            value = 1
    return longest

if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))