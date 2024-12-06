# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week: int, integers: list):
        self.week = week
        self.integers = integers

    def number_of_hits(self, numbers: list):
        return sum(1 for number in numbers if number in self.integers)
    
    def hits_in_place(self, numbers: list):
        return [number if number in self.integers else -1 for number in numbers]