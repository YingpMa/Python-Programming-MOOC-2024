# Copy here code of line function from previous exercise and use it in your solution
def line(length, text):
    if text == "":
        print("*" * length)
    else:
        print(text[0] * length)

def shape(a, character1, b, character2):
    times = 1
    while times <= a:
        line(times, character1)
        times += 1
    number = b
    while number > 0:
        line(a, character2)
        number -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")