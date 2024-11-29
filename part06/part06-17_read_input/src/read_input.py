# Write your solution here
def read_input(message: str, low: int, high: int):
    while True:
        try:
            integer = input(message)

            if int(integer) >= low and int(integer) <= high:
                return int(integer)
        except ValueError:
            pass
        print(f"You must type in an integer between {low} and {high}")