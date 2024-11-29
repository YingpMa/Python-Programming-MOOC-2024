# Write your solution here
def print_persons(filename: str):
    import json
    with open(filename) as new_file:
        data = new_file.read()
    
    people = json.loads(data)
    for person in people:
        hobbies = ''
        for hobby in person["hobbies"]:
            hobbies += hobby + ", "
        hobbies = hobbies[:-2]
        print(f"{person['name']} {person['age']} years ({hobbies})")

if __name__ == "__main__":
    filename = "file1.json"
    print_persons(filename)