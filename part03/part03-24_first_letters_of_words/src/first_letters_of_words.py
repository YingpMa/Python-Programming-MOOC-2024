# Write your solution here
# Write your solution here
sentence = input("Please type in a sentence: ")
print(sentence[0:1])
while " " in sentence:
    i = sentence.find(" ")
    sentence = sentence[i + 1:]
    print(sentence[0:1])