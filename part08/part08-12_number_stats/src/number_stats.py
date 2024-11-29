# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
        self.odd_numbers = 0
        self.even_numbers = 0

    def add_number(self, number:int):
        self.count += 1
        self.numbers += number
        if number % 2 == 0:
            self.even_numbers += number
        else:
            self.odd_numbers += number
        return self.numbers

    def count_numbers(self):
        return self.count
    
    def get_sum(self):
        return self.numbers

    def average(self):
        if self.count == 0:
            return 0
        else:
            return self.numbers / self.count

print("Please type in integer numbers: ")
stats = NumberStats()
while True:
    int_number = int(input(""))
    if int_number == -1:
        break
    stats.add_number(int_number)

print(f"Sum of numbers: {stats.numbers}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {stats.even_numbers}")
print(f"Sum of odd numbers: {stats.odd_numbers}")














