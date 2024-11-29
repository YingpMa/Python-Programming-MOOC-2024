# Write your solution here
# Write your solution here
string = input("Please type in a string: ")
character1 = string[1]
character2 = string[len(string) - 2]
if character1 == character2:
    print(f"The second and the second to last characters are {character1}")
else:
    print("The second and the second to last characters are different")