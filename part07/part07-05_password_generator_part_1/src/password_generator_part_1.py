# Write your solution here
def generate_password(amount: int):
    import string
    from random import shuffle
    string = string.ascii_lowercase
    lower = []
    for character in string:
        lower.append(character)
    shuffle(lower)
    password = ""
    for i in range(amount):
        password += lower[i]
    return password

# for i in range(10):
#     print(generate_password(8))
