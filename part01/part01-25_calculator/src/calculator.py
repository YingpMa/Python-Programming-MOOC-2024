# Write your solution here
# Write your solution here
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")
print("")
if operation == "add":
    value = number1 + number2
    print(f"{number1} + {number2} = {value}")
if operation == "multiply":
    value = number1 * number2
    print(f"{number1} * {number2} = {value}")
if operation == "subtract":
    value = number1 - number2
    print(f"{number1} - {number2} = {value}")