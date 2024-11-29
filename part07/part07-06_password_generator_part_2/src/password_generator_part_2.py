# Write your solution here
def generate_strong_password(amount: int, a: bool, b :bool):
    import string
    from random import choice, randint, shuffle
    password = ''
    string1 = string.ascii_lowercase
    string2 = string.digits
    string3 = ['!', '?', '=', '+', '-', '(', ')', '#']
    if a and b:
        list1 = [1, 2, 3]
        for i in range(amount - 3):
            list1.append(randint(1,3))
        shuffle(list1)
        for i in list1:
            if i == 1:
                password += choice(string1)
            elif i == 2:
                password += choice(string2)
            else:
                password += choice(string3)
    elif a and not b:
        list2 = [1, 2]
        for i in range(amount - 2):
            list2.append(randint(1, 2))
        shuffle(list2)
        for i in list2:
            if i == 1:
                password += choice(string1)
            else:
                password += choice(string2)
    elif not a and b:
        list3 = [1, 2]
        for i in range(amount - 2):
            list3.append(randint(1, 2))
        shuffle(list3)
        for i in list3:
            if i == 1:
                password += choice(string1)
            else:
                password += choice(string3)
    elif not a and not b:
        for i in range(amount):
            password += choice(string1)
    return password

if __name__ == "__main__":
    print(generate_strong_password(2,False,False))



