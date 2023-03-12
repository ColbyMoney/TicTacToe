from array import *

if __name__ == '__main__':
    main()

def main():
    print("im working")
    game = newGame()
    pring("im still working")
    while gameOver() == False:
        takeTurn(player)
        didWin(player)
        if player == "X":
            player = "O"
        else:
            player = "X"

class Player:
    player = "X"

class Game:
    board = [["_","_","_"], ["_","_","_"], ["_","_","_"]]

    def newGame(self):
        for x in range(0,2):
            for y in range(0,2):
                self.board[x][y] = "_"
                player = "X"

    def playGame():
        print("im working")
        game = newGame()
        pring("im still working")
        while gameOver() == False:
            takeTurn(player)
            didWin(player)
            if player == "X":
                player = "O"
            else:
                player = "X"

    def takeTurn(player):
        row = input("Select row: ")
        column = input("Select column: ")
        while board[row][column] != "_":
            print("That spot is taken! Try another spot.\n")
            row = input("Select row: ")
            column = input("Select column: ")
        board[row][column] = player

    def gameOver(game):
        return game.didWin("X") or game.didWin("O") or game.boardFull(game)

    def boardFull(game):
        for x in range(0,2):
            for y in range(0,2):
                if board[x][y] == "_":
                    return False;
        return True;

    def didWin(player):
        if (board[0][0] == player and board[0][1] == player and board[0][2] == player or 
            board[1][0] == player and board[1][1] == player and board[1][2] == player or 
            board[2][0] == player and board[2][1] == player and board[2][2] == player or

            board[0][0] == player and board[1][0] == player and board[2][0] == player or 
            board[0][1] == player and board[1][1] == player and board[2][1] == player or 
            board[0][2] == player and board[1][2] == player and board[2][2] == player or 

            board[0][0] == player and board[1][1] == player and board[2][2] == player or 
            board[2][0] == player and board[1][1] == player and board[0][2] == player):
            return True;
        return False;