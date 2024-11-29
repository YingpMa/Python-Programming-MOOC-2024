# Write your solution here
# Write your solution here
string = input("Please type in a string: ")
number = len(string) - 1
if len(string) > 0:
    while number >= 0:
        print(string[number])
        number -= 1
else:
    print("The input string is empty. There is no first character.")