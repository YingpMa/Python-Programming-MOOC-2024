def filter_solutions():
    with open("solutions.csv") as new_file:
        correct_results = []
        incorrect_results = []
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            if eval(parts[1]) == int(parts[2]):
                correct_results.append(line + "\n")
            else:
                incorrect_results.append(line + "\n")
    with open("correct.csv", "w") as my_file:
        for line in correct_results:
            my_file.write(line)
    with open("incorrect.csv", "w") as my_file:
        for line in incorrect_results:
            my_file.write(line)

           

