# Write your solution here
def hash_square(length):
    t = length
    while t > 0:
        print("#" * length)
        t -= 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)