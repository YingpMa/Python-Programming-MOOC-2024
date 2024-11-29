# Write your solution here
def cheaters():
    import csv
    from datetime import datetime
    start_times = {}
    with open("start_times.csv") as new_file:
        for line in csv.reader(new_file, delimiter=";"):
            start_times[line[0]] = datetime.strptime(line[1], "%H:%M")

    submission_times = {}   
    with open("submissions.csv") as new_file:
        for line in csv.reader(new_file, delimiter=";"):
            if line[0] not in submission_times:
                 submission_times[line[0]] = []
            submission_times[line[0]].append(datetime.strptime(line[3], "%H:%M"))

    cheaters = []
    for person, time in start_times.items():
            if person in submission_times:
                difference = 0
                for item in submission_times[person]:
                     difference = max((item - time). total_seconds() / 3600, difference)
                     
                if difference > 3:
                    cheaters.append(person)
    return cheaters





def final_points():
