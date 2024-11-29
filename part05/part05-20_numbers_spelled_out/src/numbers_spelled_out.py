# Write your solution here
def dict_of_numbers():
    dictionary = {}
    word0 = ['zero']
    wordints = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    wordteens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    wordtens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', "seventy", 'eighty', 'ninety']
    word_list = []
    for i in range(len(wordtens)):
        word_list.append(wordtens[i])
        for j in range(len(wordints)):
            word_list.append(wordtens[i] + "-" + wordints[j])
    
    word_final = []
    word_final.append(word0[0])
    for item in wordints:
        word_final.append(item)
    for item in wordteens:
        word_final.append(item)
    for item in word_list:
        word_final.append(item)

    for i in range(len(word_final)):
        dictionary[i] = word_final[i]

    return dictionary 







if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])