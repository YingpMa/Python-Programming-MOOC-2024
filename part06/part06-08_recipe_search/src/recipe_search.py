# Write your solution here
def search_by_name(filename: str, word: str):
    recipes = {}
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            if line == "":
                continue
            if line == line.capitalize() and not line.isdigit():
                name = line
                recipes[name] = []
            else:
                recipes[name].append(line)
    recipe = []
    for key in recipes:
        if word in key.lower():
            recipe.append(key)
    return recipe

def search_by_time(filename: str, prep_time: int):
    recipes = {}
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            if line == "":
                continue
            if line == line.capitalize() and not line.isdigit():
                name = line
                recipes[name] = []
            else:
                recipes[name].append(line)
    
    recipe = []
    for key, value in recipes.items():
        if prep_time >= int(value[0]):
            string = f"{key}, preparation time {value[0]} min"
            recipe.append(string)
    return recipe

def search_by_ingredient(filename: str, ingredient: str):
    recipes = {}
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            if line == "":
                continue
            if line == line.capitalize() and not line.isdigit():
                name = line
                recipes[name] = []
            else:
                recipes[name].append(line)
    recipe = []
    for key, value in recipes.items():
        if ingredient in value:
            string = f"{key}, preparation time {value[0]} min"
            recipe.append(string)
    return recipe


if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)