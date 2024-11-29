# Write your solution here
# Write your solution here
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")
letter_middle = ""
if letter1 > letter2:
    if letter2 > letter3:
        letter_middle = letter2
    else:
        if letter1 > letter3:
            letter_middle = letter3
        else:
            letter_middle = letter1
else:
    if letter3 < letter1:
        letter_middle = letter1
    else:
        if letter2 > letter3:
            letter_middle = letter3
        else:
            letter_middle = letter2
print(f"The letter in the middle is {letter_middle}")