# Write your solution here
def remove_smallest(numbers: list):
    value = numbers[0]
    for item in numbers:
        if value > item:
            value = item
    numbers.remove(value)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)