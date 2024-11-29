
def chessboard(size):
    for row in range(size):
        for col in range(size):
            if (row + col) % 2 == 0:
                print("1", end="")
            else:
                print("0", end="")
        print()
# Testing the function

if __name__ == "__main__":
    chessboard(3)
