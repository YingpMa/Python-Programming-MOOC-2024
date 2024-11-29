# Write your solution here
my_list = []
while True:
    string = input("Exam points and exercises completed: ")
    if not string:
        print("Statistics: ")
        break
    part = string.split()
    part = [int(part[0]), int(part[1])]
    my_list.append(part) 

def statistics_result(my_list: list):
    points = 0
    all_points = 0
    grade0 = 0
    string0 = ''
    grade1 = 0
    string1 = ''
    grade2 = 0
    string2 = ''
    grade3 = 0
    string3 = ''
    grade4 = 0
    string4 = ''
    grade5 = 0
    string5 = ''
    for i in range(0, len(my_list)):
        points = my_list[i][0] + int(my_list[i][1] * 0.1)
        if my_list[i][0] < 10:
            grade0 += 1
            string0 += "*"
        else:
            if points <= 14:
                grade0 += 1
                string0 += "*"
            elif points > 14 and points <= 17:
                grade1 += 1
                string1 += "*"
            elif points > 17 and points <= 20:
                grade2 += 1
                string2 += "*"
            elif points > 20 and points <= 23:
                grade3 += 1
                string3 += "*"
            elif points > 23 and points <= 27:
                grade4 += 1
                string4 += "*"
            elif points > 27 and points <= 30:
                grade5 += 1 
                string5 += "*"
        all_points += points
    points_average = all_points / len(my_list)
    pass_average = (len(my_list) - grade0) / len(my_list) * 100
    print(f"Points average: {points_average:.1f}")
    print(f"Pass percentage: {pass_average:.1f}")
    print("Grade distribution: ")
    print(f"5: {string5}" )
    print(f"4: {string4}" )
    print(f"3: {string3}" )
    print(f"2: {string2}" )
    print(f"1: {string1}" )
    print(f"0: {string0}" )
    
statistics_result(my_list) 
        



