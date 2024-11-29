# Write your solution here
# Write your solution here
story = ""
word1 = ""
while True:
    word = input("Please type in a word: ")
    if word == 'end':
        print(story)
        break
    if  word1 == word:
        print(story)
        break
    story += word + " "
    word1 = word
    