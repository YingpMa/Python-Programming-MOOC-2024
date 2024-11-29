# Write your solution here
def lottery_numbers(amount: int, lower: int, upper: int):
    from random import randint
    numbers = []
    while len(numbers) < amount:
        number = randint(lower, upper)
        if number not in numbers:
            numbers.append(number)
    return sorted(numbers)

