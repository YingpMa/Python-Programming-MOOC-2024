# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
        self.days = year * 360 + month * 30 + day

    def __lt__(self, another):
        return self.days < another.days
    
    def __gt__(self, another):
        return self.days > another.days
    
    def __eq__(self, another):
        return self.days == another.days
    
    def __ne__(self, another):
        return self.days != another.days
    
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __add__(self, days: int):
        days = self.days + days
        year = days // 360
        month = (days - year * 360) // 30
        day = (days - year * 360) % 30
        return SimpleDate(day, month, year)
    
    def __sub__(self, another):
        days = abs(self.days - another.days)
        return days

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)

    d3 = d1 + 3
    d4 = d2 + 400

    print(d1)
    print(d2)
    print(d3)
    print(d4)