import os
import time

board = [["   ", "   ", "   "],
         ["   ", "   ", "   "],
         ["   ", "   ", "   "]]

symbols_chosen = False
player_1 = ""
player_2 = ""

while not symbols_chosen:
    print("Welcome to Tic Tac Toe Game!")
    print("Please choose the symbol you will play.")
    player_1 = input("Player 1, please choose X or O:")
    if player_1 == "X":
        player_1 = " X "
        player_2 = " O "
        symbols_chosen = True
    elif player_1 == "O":
        player_1 = " O "
        player_2 = " X "
        symbols_chosen = True
    else:
        print("You need to choose from X or O only.")


def print_board(board_):
    i = 0
    for row in board:
        print(" | ".join(row))
        i += 1
        if i < 3:
            print("-" * 3, "+", "-" * 3, "+", "-" * 3)


def check_winner(board_, player):
    # Check rows
    for row in board_:
        if all([spot == player for spot in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board_[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board_[i][i] == player for i in range(3)]) or all([board_[i][2 - i] == player for i in range(3)]):
        return True
    return False


def check_draw(board_):
    return all([spot != "   " for row in board_ for spot in row])


def next_step(player):
    step_row = int(input(f"Choose row for next step (1 - 3):"))
    step_col = int(input("Choose column for next step (1 - 3):"))
    if 0 <= step_row - 1 <= 2 and 0 <= step_col - 1 <= 2:
        if board[step_row - 1][step_col - 1] == "   ":
            board[step_row - 1][step_col - 1] = player
        else:
            print("Choose another.")
            next_step(player)
    else:
        print("You need to choose row and column in range of board.")
        time.sleep(1)
        next_step(player)


step = 1

while True:
    os.system('clear')
    print_board(board)
    if check_winner(board, player_1):
        print(f"Player 1 wins!")
        break
    elif check_winner(board, player_2):
        print(f"Player 2 wins!")
        break
    elif check_draw(board):
        print(f"It's draw.")
        break
    else:
        if step % 2 != 0:
            print("Next step will make Player 1.")
            next_step(player_1)
        else:
            print("Next step will make Player 2.")
            next_step(player_2)
        step += 1
