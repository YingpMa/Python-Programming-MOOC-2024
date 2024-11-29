
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

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

            
    
for key, value in names.items():
    if key in exercises:
        exercise = exercises[key]
        print(f"{names[key]} {exercise}")
