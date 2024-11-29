# Write your solution here
def histogram(string: str):
    groups = {}
    for character in string:
        if character not in groups:
            groups[character] = 0
        groups[character] += 1
    for key, value in groups.items():
        print(key, "*" * value)

if __name__ == "__main__":
    string = "statistically"
    histogram(string)