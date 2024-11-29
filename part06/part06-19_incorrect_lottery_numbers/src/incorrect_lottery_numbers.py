# Write your solution here
def filter_incorrect():
    dictionary = {}
    with open("lottery_numbers.csv") as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            week = parts[0][5:]
            numbers = parts[1].split(",")
            try:
                week = int(week)
                numbers = [int(num) for num in numbers]
                new_numbers = []
                for num in numbers:
                    if num not in new_numbers and num >= 1 and num <= 39:
                        new_numbers.append(num)
                if len(new_numbers) == 7:
                    dictionary[week] = numbers

            except (ValueError, IndexError):
                pass
    
    with open("correct_numbers.csv", "w") as my_file:
        for key, value in dictionary.items():
            my_file.write(f"week {key};{value[0]},{value[1]},{value[2]},{value[3]},{value[4]},{value[5]},{value[6]}\n")



