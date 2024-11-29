# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv", "a") as new_file:
        string = f"{person[0]};{person[1]};{person[2]}\n"
        new_file.write(string)