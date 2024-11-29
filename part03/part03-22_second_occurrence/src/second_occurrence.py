# Write your solution here
# Write your solution here
string = input("Please type in a string: ")
substring =input("Please type in a substring: ")
index = string.find(substring)
if index != -1:
    string = string[index +len(substring):]
    a = index
    index = string.find(substring)
    if index != -1:
        print(f"The second occurrence of the substring is at index {index + a + len(substring) }.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")
