# Write your solution here
# Write your solution here
number = int(input("Please type in a number: "))
a = 1 
while a <= number:
    i = 1
    while i <= number:
        print(f"{a} x {i} = {a * i}")
        i +=1
    a += 1