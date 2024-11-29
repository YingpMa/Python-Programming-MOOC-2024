# Write your solution here
# Write your solution here
gift = int(input("Value of gift: "))
tax = 0
if gift >= 5000 and gift < 25000:
    tax = (gift - 5000) * 0.08 + 100
elif gift >= 25000 and gift < 55000:
    tax = (gift - 25000) * 0.1 + 1700
elif gift >= 55000 and gift <200000:
    tax = (gift - 55000) * 0.12 + 4700
elif gift >= 200000 and gift < 1000000:
    tax = (gift - 200000) * 0.15 + 22100
elif gift >= 1000000:
    tax = 142100 + (gift - 1000000) * 0.17

if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")
