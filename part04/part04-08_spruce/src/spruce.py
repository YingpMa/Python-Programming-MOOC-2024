# Write your solution here
def spruce(i):
    print("a spruce!")
    t = 1
    a = i
    while a > 0:
        print(" " * (a-1) + "*" * (t * 2 - 1 ))
        a -= 1
        t += 1
    print(" " * (i-1) + "*" )
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)