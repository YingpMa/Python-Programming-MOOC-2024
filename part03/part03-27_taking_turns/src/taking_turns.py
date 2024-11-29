# Write your solution here
# Write your solution here
number = int(input("Please type in a number: "))
t = 0
if number == 1:
    print(number)
elif number % 2 == 0:
    while (1 + t) < (number - t):
        print(1 + t)
        print(number - t)
        t += 1
elif number % 2 != 0:
    while t < int(number/2):
        print(1 + t)
        print(number - t)
        t += 1
    print(1 + t)