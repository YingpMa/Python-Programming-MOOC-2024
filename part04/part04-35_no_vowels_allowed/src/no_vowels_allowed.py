# Write your solution here
def no_vowels(my_string: str):
    new_string = ''
    for character in my_string:
        if character != 'a' and character != 'e' and character != 'i' and character != 'o' and character != 'u':
            new_string = f"{new_string}{character}"
    return new_string

if __name__ == "__main__":
    string1 = "this is an example"
    print(no_vowels(string1))