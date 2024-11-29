# Write your solution here
# Write your solution here
number = int(input("Please type in a number: "))
n = number
factorial = 1
while number > 0 :
    while n > 0:
        factorial *= n
        n -= 1
    print(f"The factorial of the number {number} is {factorial}")
    number = int(input("Please type in a number: "))
    factorial = 1
    n = number
print("Thanks and bye!")    
