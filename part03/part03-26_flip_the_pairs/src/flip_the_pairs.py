# Write your solution here
# Write your solution here
number = int(input("Please type in a number: "))
i = 1
if number == 1:
    print(i)
elif number % 2 ==0:
    while number > i:
        print(i+1)
        print(i)
        i += 2
else:
    while number > i:
        print(i+1)
        print(i)
        i += 2
    print(number)