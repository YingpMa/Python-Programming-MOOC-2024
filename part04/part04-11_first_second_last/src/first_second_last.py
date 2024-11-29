# Write your solution here
def first_word(sentence):
    a = sentence.find(" ")
    return sentence[:a]
def second_word(sentence):
    a = sentence.find(" ")
    if sentence.find(" ") == sentence.rfind(" "):
        return sentence[a+1:]
    else:
        sentence = sentence[a+1:]
        a = sentence.find(" ")
        return sentence[:a]
def last_word(sentence):
    a = sentence.rfind(" ")
    return sentence[a+1:]
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))