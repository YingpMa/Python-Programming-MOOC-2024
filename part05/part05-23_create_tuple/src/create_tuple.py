# Write your solution here
def create_tuple(x: int, y: int, z: int):
    min_value = min(x, y, z)
    max_value = max(x, y, z)
    mean = x + y + z
    point = (min_value, max_value, mean)
    return point

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))