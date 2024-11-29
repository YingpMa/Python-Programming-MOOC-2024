# Write your solution here
# Write your solution here
word =input("Please type in a word: ")
character = input("Please type in a character: ")
a = word.find(character)
if character in word and len(word) - a >= 3:
    print(word[a:a +3])