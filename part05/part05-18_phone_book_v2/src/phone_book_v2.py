# Write your solution here
phone_book = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 2:
        name = input("name: ")
        numebr = input("number: ")
        if name not in phone_book:
            phone_book[name] = []
        phone_book[name].append(numebr)
        print("ok!")
    if command == 1:
        name = input("name: ")
        if name in phone_book:
            for item in phone_book[name]:
                print(item)
        else:
            print("no number")
    if command == 3:
        break

print("quitting...")