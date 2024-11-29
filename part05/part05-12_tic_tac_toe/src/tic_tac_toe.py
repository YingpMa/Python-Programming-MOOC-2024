# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if x not in range(0,3) or y not in range(3):
        return False
    if not isinstance(piece, str) or piece not in ["X", "O"]:
        return False
    if game_board[y][x] in ["X", "O"]:
        return False
    else:
        game_board[y][x] = piece
    return True

if __name__ =="__main__":
    game_board = [['X', 'O', ''], ['X', 'O', 'O'], ['', '', '']]
    print(play_turn(game_board, 1, 1, 0))
    print(game_board)
