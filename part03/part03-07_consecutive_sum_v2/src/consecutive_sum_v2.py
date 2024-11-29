# Write your solution here
# Write your solution here
limit = int(input("Limit: "))
sum = 0
number = 1
sentence ="The consecutive sum: "
while sum < limit:
    sum += number
    if sum < limit:
        sentence += f"{number} + " 
    else:
        sentence += f"{number} = {sum} " 
    number += 1
print(sentence)