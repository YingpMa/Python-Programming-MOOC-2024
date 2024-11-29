# Write your solution here
def add_student(students: dict, name: str):
    students[name] = None

def print_student(students: dict, name: str):
    if name in students:
        print(name + ":")
        if students[name] == None:
            print(" no completed courses")
        else:
            courses = students[name]
            print(f" {len(courses)} completed courses:")
            grade = 0
            for item in courses:
                grade += item[1]
                print(f"  {item[0]} {item[1]}")
            ave_grade = grade / len(courses)
            print(f" average grade {ave_grade}")
        
    else:
        print(f"{name}: no such person in the database")

def add_course(students: dict, name: str, course: tuple):
    if name in students:
        if course[1] == 0:
            return
        if students[name] == None:
            students[name] = []
        for i,item in enumerate(students[name]):
            if course[0] in item:
                if course[1] > item[1]:
                    students[name][i] = item[0], course[1]
                return
            
        students[name].append(course)

def summary(students: dict):
    print(f"students {len(students)}")
    number = 0
    student1 = ''
    student2 = ''
    best_grade = 0
    for key, value in students.items():
        if len(value) > number:
            number = len(value)
            student1 = key
        total_grade = 0
        ave_grade = 0
        for item in value:
            total_grade += item[1]
        ave_grade = total_grade / len(value)
        if best_grade < ave_grade:
            best_grade = total_grade / len(value)
            student2 = key     
    print(f"most courses completed {number} {student1}")
    print(f"best average grade {best_grade} {student2}")
        

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)