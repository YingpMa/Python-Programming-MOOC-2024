# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        numbers = []
        for number in new_file:
            number = number.replace("\n", "")
            number = int(number)
            numbers.append(number)
        numbers.sort()
    return numbers[-1]