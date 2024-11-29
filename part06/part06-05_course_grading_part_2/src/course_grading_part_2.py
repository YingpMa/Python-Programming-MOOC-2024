# wwite your solution here

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")


names = {}
with open(student_info) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(';')
        if parts[0] == "id":
            continue
        names[parts[0]] = parts[1] + " " + parts[2]

exercises = {}
with open(exercise_data) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(";")
        numbers = 0
        if parts[0] == "id":
            continue
        for i in range(1, 8):
            numbers += int(parts[i])
        exercises[parts[0]] = numbers

exams = {}
with open(exam_points) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exams[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3])

for key, value in exams.items():
    if key in exercises:
        if exercises[key] < 4:
            continue
        elif exercises[key] >= 4 and exercises[key] < 8:
            exams[key] += 1
        elif exercises[key] >= 8 and exercises[key] < 12:
            exams[key] += 2
        elif exercises[key] >= 12 and exercises[key] < 16:
            exams[key] += 3
        elif exercises[key] >= 16 and exercises[key] < 20:
            exams[key] += 4
        elif exercises[key] >= 20 and exercises[key] < 24:
            exams[key] += 5
        elif exercises[key] >= 24 and exercises[key] < 28:
            exams[key] += 6
        elif exercises[key] >= 28 and exercises[key] < 32:
            exams[key] += 7
        elif exercises[key] >= 32 and exercises[key] < 36:
            exams[key] += 8
        elif exercises[key] >= 36 and exercises[key] < 40:
            exams[key] += 9
        elif exercises[key] == 40:
            exams[key] += 10

grades = {}

for key, value in exams.items():
    if value >= 0 and value < 15:
        grades[names[key]] = 0
    elif value >= 15 and value < 18:
        grades[names[key]] = 1
    elif value >= 18 and value < 21:
        grades[names[key]] = 2
    elif value >= 21 and value < 24:
        grades[names[key]] = 3
    elif value >= 24 and value < 28:
        grades[names[key]] = 4
    elif value >= 28:
        grades[names[key]] = 5

for key, value in grades.items():
    print(f"{key} {value}")
