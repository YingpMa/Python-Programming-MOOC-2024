# Write your solution here
def separate_characters(my_string: str):
    import string
    string0 = ''
    string1 = ''
    string2 = ''
    for character in my_string:
        if character in string.ascii_letters:
            string0 += character
        elif character in string.punctuation:
            string1 += character
        else:
            string2 += character
    parts = (string0, string1, string2)
    return parts