# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    persons = [person1, person2, person3]
    small = 30
    for item in persons:
        results = 0
        for key, value in item.items():
            if key != "name":
                results += value
        if small > results:
            small = results
            person = item 
    return person

if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))
                 


        