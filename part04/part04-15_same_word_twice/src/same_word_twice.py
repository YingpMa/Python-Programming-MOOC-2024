# Write your solution here
myword = []
while True:
    word = input("Word: ")
    if word in myword:
        break
    myword.append(word)

print(f"You typed in {len(myword)} different words")