# Write your solution here
# Write your solution here
word = input("Word: ")
print("*" * 30)
print("*" + " " * (14-int(len(word)/2)), end = "")
print(word, end="")
print(" " * (14 + int(len(word) / 2)-len(word))+ "*")
print("*" * 30)