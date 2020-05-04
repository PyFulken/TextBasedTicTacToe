#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def TicTacToe():
    Board = [["1","2","3"],["4","5","6"],["7","8","9"]] #Board reset
    def print_board (Player):
        print("",Board[0][0], "|", Board[0][1], "|", Board[0][2], "\n", "--+---+--", "\n",Board[1][0], "|", Board[1][1], "|", Board[1][2],"\n","--+---+--","\n",Board[2][0], "|", Board[2][1], "|", Board[2][2], "\nPlayer %s's turn!"%Player, "\nWhere should your piece go?") #Prints a pretty board
    def victory_check():
        if Board[0][0] == Board[0][1] == Board[0][2] or Board[1][0] == Board[1][1] == Board[1][2] or Board[2][0] == Board[2][1] == Board[2][2] or Board[0][0] == Board[1][0] == Board[2][0] or Board[0][1] == Board[1][1] == Board[2][1] or Board[0][2] == Board[1][2] == Board[2][2] or Board[0][0] == Board[1][0] == Board[2][0] or Board[0][1] == Board[1][1] == Board[2][1] or Board[0][0] == Board[1][1] == Board[2][2] or Board[2][0] == Board[1][1] == Board[0][2]: #Rafa disse que isto é um pattern, deve dar para encurtar!
            print("Player %s Wins!" %Player)
            print("",Board[0][0], "|", Board[0][1], "|", Board[0][2], "\n", "--+---+--", "\n",Board[1][0], "|", Board[1][1], "|", Board[1][2],"\n","--+---+--","\n",Board[2][0], "|", Board[2][1], "|", Board[2][2])
            return True
        else:
            return False
    def piece_placement (Player):
        helper = int(input())
        while helper > 9 or helper < 1:
            print("There's no such position!")
            helper = int(input())
        col, row = divmod(helper-1,3)
        while Board[col][row] == "X" or Board[col][row] == "O":
            print("That space is already filled!")
            helper = int(input())
            col, row = divmod(helper-1,3)
        else:
            if Player == 1:
                Piece = "X"
            else:
                Piece = "O"
            Board[col][row] = Piece
    for turno in range(1,10): #So há 9 turnos possiveis no Tic Tac Toe, não há mais posições no board.
        if turno%2!=0: #Turno do jogador 1
            Player = 1
            print_board(Player)
            piece_placement(Player)
            if victory_check():
                break
        if turno%2==0: #Turno do jogador 2
            Player = 2
            print_board(Player)
            piece_placement(Player)
            if victory_check():
                break
TicTacToe()
Restart = input("Would you like to play another game? (Y,N)")
while Restart == "Y" or Restart == "y":
    TicTacToe()
    Check = input("Would you like to play another game? (Y,N)")
    if Check == "N" or Check == "n":
        Restart = False
print("Game Over!")
#Why does it always save the checkpoints?!?!?!?

