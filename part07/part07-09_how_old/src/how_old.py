# Write your solution here
from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birth_date = datetime(year, month, day)
time_millennium = datetime(1999, 12, 31)
difference = time_millennium -birth_date
if difference.days > 0:
    print(f"You were {difference.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")