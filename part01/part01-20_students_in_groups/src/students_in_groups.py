# Write your solution here
# Write your solution here
students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
number_of_group = students / group_size
if number_of_group == students // group_size:
    print(f"Number of groups formed: {number_of_group}")
else:
    print(f"Number of groups formed: {students // group_size + 1}")