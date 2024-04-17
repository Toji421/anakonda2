def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    while True:
        print_board(board)
        player = players[turn % 2]
        row, col = map(int, input(f"Ход игрока {player}. Введите номер строки и столбца (например, '1 1' для первой строки, первого столбца): ").split())
        if board[row-1][col-1] == " ":
            board[row-1][col-1] = player
            if check_winner(board, player):
                print_board(board)
                print(f"Игрок {player} выиграл!")
                break
            if all(all(cell != " " for cell in row) for row in board):
                print_board(board)
                print("Ничья!")
                break
            turn += 1
        else:
            print("Эта клетка уже занята. Пожалуйста, выберите другую.")

if __name__ == "__main__":
    tic_tac_toe()
