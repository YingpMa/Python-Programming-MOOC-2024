# write your solution here
wordlist = []
with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.strip()
        wordlist.append(line)

# print(wordlist)

text = input("Write text: ")
text_word = text.split(" ")
# print(text_word)
checkword = ""
for word in text_word:
    if word.lower() in wordlist:
        checkword += word + " " 
    else:
        checkword += "*" + word + "* "
print(checkword)