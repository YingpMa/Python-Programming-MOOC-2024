# Write your solution here
def find_movies(database: list, search_term: str):
    all_name = []
    for item in database:
        all_name.append(item["name"])
    search_name = []
    for item in all_name:
        if search_term.lower() in item.lower():
            search_name.append(item)
    search_result = []
    for item in database:
        if item["name"] in search_name:
            search_result.append(item)
    return search_result         

if __name__ == "__main__":
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)    
