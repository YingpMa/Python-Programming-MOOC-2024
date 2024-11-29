# Write your solution here
# Write your solution here
year = int(input("Year: "))
leap_year = year
while True:
    if (leap_year % 4 == 0 and leap_year % 100 != 0) or leap_year % 400 == 0:
        if year == leap_year:
            leap_year += 4
        break
    leap_year += 1

if (leap_year % 4 == 0 and leap_year % 100 != 0) or leap_year % 400 == 0:
    leap_year = leap_year
else:
    leap_year += 4

print(f"The next leap year after {year} is {leap_year}")