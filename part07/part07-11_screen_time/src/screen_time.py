# Write your solution here
from datetime import datetime, timedelta
filename = input("Filename: ")
date_begin = input("Starting date: ")
date_begin = datetime.strptime(date_begin, "%d.%m.%Y")

days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
screen_time = {}
for i in range(days):
    day = date_begin + timedelta(days = i)
    day = day.strftime("%d.%m.%Y")
    time = input(f"Screen time {day}: ")
    time = time.split(" ")
    screen_time[day] = []
    for item in time:
        screen_time[day].append(int(item))

with open(filename, "w") as my_file:
    date_end = date_begin + timedelta(days = (days -1))
    my_file.write(f"Time period: {date_begin.strftime('%d.%m.%Y')}-{date_end.strftime('%d.%m.%Y')}\n")
    total_minutes = 0
    for key, value in screen_time.items():
        total_minutes +=sum(value)
    my_file.write(f"Total minutes: {total_minutes}\n")
    ave_minutes = total_minutes / days
    my_file.write(f"Average minutes: {ave_minutes}\n")
    for key, value in screen_time.items():
        string = key + ": "
        for number in value:
            string += str(number) +"/"
        string = string[:-1] + "\n"
        my_file.write(string)

print(f"Data stored in file {my_file}")   

