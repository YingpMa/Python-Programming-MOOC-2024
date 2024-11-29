# Write your solution here
def factorials(n: int):
    k = {}
    for i in range(1, n + 1):
        value = 1
        for j in range (1, n + 1):
            value *= j
            k[j] = value
    return k

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])