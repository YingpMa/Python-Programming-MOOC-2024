# Write your solution here
times = float(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
groceries_expenditure = float(input("How much money do you spend on groceries in a week? "))
expenditure = times * price + groceries_expenditure
print("")
print("Average food expenditure:")
print(f"Daily: {expenditure / 7} euros")
print(f"Weekly: {expenditure} euros")
