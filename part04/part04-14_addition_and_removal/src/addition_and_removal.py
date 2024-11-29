# Write your solution here
list1 = []
print(f"The list is now {list1}")
while True:
    choice = input("a(d)d, (r)emove or e(x)it: ")
    i = 0
    length = 0
    if choice == 'd' and list1 == []:
        list1.append(1)
        print(f"The list is now {list1}")
    elif choice == 'd':
        i = list1[len(list1) - 1] + 1
        list1.append(i)
        print(f"The list is now {list1}")
    elif choice == 'r':
        list1.pop(len(list1) -1)
        print(f"The list is now {list1}")
    if choice == "x":
        print("Bye! ")
        break
