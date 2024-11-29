# Write your solution here
def roll(die: str):
    from random import choice
    list_a = [3, 3, 3, 3, 3, 6]
    list_b = [2, 2, 2, 5, 5, 5]
    list_c = [1, 4, 4, 4, 4, 4]
    if die == "A":
        return choice(list_a)
    elif die == "B":
        return choice(list_b)
    else:
        return choice(list_c)

def play(die1: str, die2: str, times: int):
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(times):
        m = roll(die1)
        n = roll(die2)
        if m > n:
            count1 += 1
        elif m < n:
            count2 += 1
        else:
            count3 += 1
    result = (count1, count2, count3)
    return result

if __name__ == "__main__":
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
