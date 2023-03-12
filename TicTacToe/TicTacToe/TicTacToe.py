print("Hello world")

def main():
    playGame()

class Player:
    player = "X"
    wins = 0

class Game:
    row = ["_","_","_"]
    board = row[3]

    def newGame(self):
        for x in range(0,2):
            for y in range(0,2):
                self.board[x][y] = "_"
                player = "X"

    def takeTurn(player):
        row = input("Select row: ")
        column = input("Select column: ")
        while board[row][column] != "_":



        if board[row][column] == "_":
            board[row][column] = player
        else while board[row][column] != 


    def playGame():
        game = newGame()

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
    