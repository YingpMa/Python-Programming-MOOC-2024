# Write your solution here
phone_book = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 2:
        name = input("name: ")
        numebr = input("number: ")
        phone_book[name] = numebr
        print("ok!")
    if command == 1:
        name = input("name: ")
        if name in phone_book:
            print(phone_book[name])
        else:
            print("no number")
    if command == 3:
        break

print("quitting...")