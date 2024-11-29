# Write your solution here
def find_words(search_term: str):
    wordlist = []
    results = []
    with open("words.txt") as new_file:
        for line in new_file:
            line = line.strip()
            wordlist.append(line)
        
    for word in wordlist:
        if "*" == search_term[0]:
            if search_term[1:] == word[-len(search_term) + 1:]:
                results.append(word)
        elif "*" == search_term[-1]:
            if search_term[:-1] == word[:len(search_term) - 1]:
                results.append(word)
        elif "." in search_term:
            if len(word) == len(search_term):
                match = True
                for i in range(len(search_term)):
                    if search_term[i] != "." and search_term[i] != word[i]:
                        match = False
                        break
                if match:
                        results.append(word)
        else:
            if word == search_term:
                results.append(word)
    return results



