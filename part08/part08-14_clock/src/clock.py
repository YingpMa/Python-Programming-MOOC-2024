# Write your solution here:
# Write your solution here:
from datetime import timedelta, datetime

class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
    
    def tick(self):
        if self.hours == 23 and self.seconds == 59 and self.minutes == 59:
            self.minutes = 0
            self.seconds = 0
            self.hours = 0
        elif self.seconds == 59 and self.minutes == 59:
            self.minutes == 0
            self.seconds == 0
            self.hours += 1
        elif self.seconds  == 59:
            self.minutes += 1
            self.seconds = 0
        else:
            self.seconds += 1
    
    def set(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

if __name__ == "__main__":
    clock = Clock(12, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)