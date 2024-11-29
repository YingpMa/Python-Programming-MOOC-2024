# WRITE YOUR SOLUTION HERE:
class ListHelper:
    
    @classmethod
    def greatest_frequency(cls, my_list: list):
        numbers = {}
        for item in my_list:
            if item not in numbers:
                numbers[item] = 0
            numbers[item] +=1


        m = 0
        n = 0
        for number, frequency in numbers.items():
            if frequency > m:
                m = frequency
                n = number
        return n
    
    @classmethod
    def doubles(cls, my_list: list):
        numbers = {}
        for item in my_list:
            if item not in numbers:
                numbers[item] = 0
            numbers[item] +=1

        i = 0
        for number, frequency in numbers.items():
            if frequency >= 2:
                i +=1

        return i
    
if __name__ == "__main__":

    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
