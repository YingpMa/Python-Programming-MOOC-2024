# Write your solution here
def words(n: int, beginning: str):
    from random import shuffle
    dictionary = []
    wordlist = []
    with open("words.txt") as my_file:
        for line in my_file:
            line = line.strip()
            dictionary.append(line)
    
    for word in dictionary:
        if beginning == word[:len(beginning)]:
            wordlist.append(word)
    
    if len(wordlist) < n:
        raise ValueError
    else:
        shuffle(wordlist)
        wordlist = wordlist[:n]
    return wordlist
    
        


