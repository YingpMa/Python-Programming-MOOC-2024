# Write your solution here
def who_won(game_board: list):
    count1 = 0
    count2 = 0
    for row in game_board:
        for i in row:
            if i == 1:
                count1 += 1
            elif i == 2:
                count2 += 1
    if count1 > count2:
        return 1
    elif count1 < count2:
        return 2
    else:
        return 0