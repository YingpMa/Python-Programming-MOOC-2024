# tee ratkaisusi tänne
class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def name(self):
        return self.__name

    def grade(self):
        return self.__grade

    def credits(self):
        return self.__credits
    
    def update_grade(self, grade: int):
        if grade > self.__grade:
            self.__grade = grade
        
class CourseRecord:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self.__courses:
            self.__courses[name] = Course(name, grade, credits)
        else:
            self.__courses[name].update_grade(grade)

    def get_entry(self, name: str):
        if name not in self.__courses:
            return None
        return self.__courses[name]

    def all_entries(self):
        return self.__courses
    
class CourseRecordApplication:
    def __init__(self):
        self.__courserecord = CourseRecord()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__courserecord.add_course(name, grade, credits)

    def search(self):
        name = input("course: ")
        course = self.__courserecord.get_entry(name)
        if course is None:
            print("no entry for this course")
            return
        print(f"{name} ({course.credits()} cr) grade {course.grade()}")

    def statistics(self):
        num_courses = len(self.__courserecord.all_entries())
        total_credits = 0
        total_grades = 0
        courses = {1: "", 2: "", 3: "", 4: "", 5: ""}
        for key, value in self.__courserecord.all_entries().items():
            total_credits += value.credits()
            total_grades += value.grade()
            courses[value.grade()] += "x"
        mean = total_grades / num_courses
        print(f"{num_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")
        for key, value in courses.items():
            print(f"{key}: {value}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.search()
            elif command == "3":
                self.statistics()
            else:
                self.help()

application = CourseRecordApplication()
application.execute()