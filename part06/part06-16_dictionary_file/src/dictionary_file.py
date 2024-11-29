# Write your solution here
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = int(input("Function: "))
    if function == 1:
        with open("dictionaey.txt", "a") as new_file:
            word1 = input("The word in English: ")
            word2 = input("The word in English: ")
            new_file.write(f"{word1};{word2}\n")
        print("Dictionary entry added")
    if function == 2:
        with open("dictionaey.txt") as new_file:
            term = input("Search term: ")
            dictionary = []
            for line in new_file:
                line = line.strip()
                dictionary.append(line.replace(";", " - "))
            for word in dictionary:
                if term in word:
                    print(word)
    if function == 3:
        print("Bye!")
        break
