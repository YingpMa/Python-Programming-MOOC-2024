# Write your solution here
# Write your solution here
hourly_wage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ")
if day == "Sunday":
    daily_wages = hourly_wage * hours * 2
else:
    daily_wages = hourly_wage * hours
print(f"Daily wages: {daily_wages} euros")