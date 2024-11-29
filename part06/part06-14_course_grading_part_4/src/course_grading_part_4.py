
# student_info = "students2.csv"
# exercise_data = "exercises2.csv"
# exam_points = "exam_points2.csv"
# course_info = "course2.txt"
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")
course_info = input("Course information: ")

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


total_points ={}

for key, value in exams.items():
    if key in exercises:
        if exercises[key] < 4:
            total_points[key] = value
        elif exercises[key] >= 4 and exercises[key] < 8:
            total_points[key] = value + 1
        elif exercises[key] >= 8 and exercises[key] < 12:
            total_points[key] = value + 2
        elif exercises[key] >= 12 and exercises[key] < 16:
            total_points[key] = value + 3
        elif exercises[key] >= 16 and exercises[key] < 20:
            total_points[key] = value + 4
        elif exercises[key] >= 20 and exercises[key] < 24:
            total_points[key] = value + 5
        elif exercises[key] >= 24 and exercises[key] < 28:
            total_points[key] = value + 6
        elif exercises[key] >= 28 and exercises[key] < 32:
            total_points[key] = value + 7
        elif exercises[key] >= 32 and exercises[key] < 36:
            total_points[key] = value + 8
        elif exercises[key] >= 36 and exercises[key] < 40:
            total_points[key] = value + 9
        elif exercises[key] == 40:
            total_points[key] = value + 10

grades = {}

for key, value in total_points.items():
    if value >= 0 and value < 15:
        grades[key] = 0
    elif value >= 15 and value < 18:
        grades[key] = 1
    elif value >= 18 and value < 21:
        grades[key] = 2
    elif value >= 21 and value < 24:
        grades[key] = 3
    elif value >= 24 and value < 28:
        grades[key] = 4
    elif value >= 28:
        grades[key] = 5

course = []

with open(course_info) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(": ")
        course.append(parts[1])

    
with open("results.txt", "w") as my_file:
    string = f"{course[0]}, {course[1]} credits"
    my_file.write(string + "\n")
    my_file.write("=" * len(string) + "\n")
    my_file.write("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n")
    for key, value in grades.items():
        my_file.write(f"{names[key]:30}{exercises[key]:<10}{(total_points[key] - exams[key]):<10}{exams[key]:<10}{total_points[key]:<10}{value:<10}\n")

with open("results.csv", "w") as my_file:
    for key, value in grades.items():
        string = f"{key};{names[key]};{value}\n"
        my_file.write(string)

print("Results written to files results.txt and results.csv")