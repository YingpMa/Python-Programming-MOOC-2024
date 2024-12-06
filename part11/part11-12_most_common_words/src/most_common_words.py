# WRITE YOUR SOLUTION HERE:
import re
def most_common_words(filename: str, lower_limit: int):
    filelist = []
    with open(filename) as my_file:
        for sentence in my_file:
            sentence = sentence.replace("\n", "")
            sentence = re.sub(r"[,.!?]", "", sentence)
            parts = sentence.split()
            for part in parts:
                filelist.append(part)

    return {word: filelist.count(word) for word in filelist if filelist.count(word) >= lower_limit}
        