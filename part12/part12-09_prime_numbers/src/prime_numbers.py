# Write your solution here
def prime_numbers():
    number = 2
    while True:
        boolean = True
        for i in range(2, number):
            if number % i == 0:
                boolean = False
        if boolean:
            yield number
        number += 1

