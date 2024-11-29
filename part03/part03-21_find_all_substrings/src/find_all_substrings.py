# Write your solution here
# Write your solution here
word = input("Please type in a word: ")
character =input("Please type in a character: ")
while True:
    a = word.find(character)
    if character in word and len(word) - a >= 3:
        print(word[a:a +3])
    else:
        break
    word = word[a+1:]