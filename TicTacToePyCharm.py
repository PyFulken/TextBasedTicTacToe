from TextBasedTicTacToe.TextBasedTicTacToe.input_sanitize import input_int_positive
from IPython.display import clear_output


def TicTacToe():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def print_board():
        print("", board[0], "|", board[1], "|", board[2])
        print("---+---+---")
        print("", board[3], "|", board[4], "|", board[5])
        print("---+---+---")
        print("", board[6], "|", board[7], "|", board[8])

    def victory_check(piece):
        if board[0] == board[1] == board[2] == piece or \
                board[3] == board[4] == board[5] == piece or \
                board[6] == board[7] == board[8] == piece or \
                board[0] == board[3] == board[6] == piece or \
                board[1] == board[4] == board[7] == piece or \
                board[2] == board[5] == board[8] == piece or \
                board[0] == board[4] == board[8] == piece or \
                board[2] == board[4] == board[6] == piece:
            print_board()
            print(f"Player {player} Wins!")
            return True

    def piece_placement(piece):
        helper = input_int_positive()
        while helper > 9 or helper < 1:
            clear_output()
            print_board()
            print("There's no such position!")
            helper = input_int_positive()
        while board[helper - 1] != " ":
            print("That space is already filled! Please choose another position")
            clear_output()
            print_board()
            helper = input_int_positive()
        else:
            board[helper - 1] = piece

    for turno in range(1, 11):
        if turno == 10:
            print("You're all out of positions to place more pieces."
                  "It's a draw!")
            break
        if turno % 2 != 0:
            player = 1
            clear_output()
            print_board()
            print(f"where will you be placing your piece, player {player}?")
            piece_placement("X")
            if victory_check("X"):
                break
        else:
            player = 2
            clear_output()
            print_board()
            print(f"where will you be placing your piece, player {player}?")
            piece_placement("O")
            if victory_check("O"):
                break


def restart_check():
    restart = input("Would you like to play another game? (Y,N)")
    while restart.lower() != "y" or restart.lower() != "n":
        restart = input("The valid inputs are either Y or N.")
    while restart.lower() == "y":
        TicTacToe()
        recheck = input("Would you like to play another game? (Y,N)")
        if recheck.lower() == "n":
            restart = False


TicTacToe()
restart_check()
