#simple Tic-Tac-Toe in python       # arranja
import time

def checkDiagonal(board, symbol):
    for d in range(0, 2):
        d *= 2
        if board[0 + d] == board[4] == board[8 - d] == symbol:
            return True


def checkColumn(board, symbol):
    for c in range(0, 3):
        if board[0 + c] == board[3 + c] == board[6 + c] == symbol:
            return True


def checkRow(board, symbol):
    for r in range(0, 3):
        r *= 3
        if board[0 + r] == board[1 + r] == board[2 + r] == symbol:
            return True


def choosePlayer(index):
    if index % 2 == 0:
        player = "Player2"
        symbol = "O"
    else:
        player = "Player1"
        symbol = "X"
    return player, symbol


def printBoard(player, board):
    print(f"""

             {player}'s Turn!

                |       |  
            {board[0]}   |   {board[1]}   |   {board[2]}
                |       |       
        ------------------------        1 | 2 | 3 
                |       |              -----------
            {board[3]}   |   {board[4]}   |   {board[5]}           4 | 5 | 6 
                |       |              -----------
        ------------------------        7 | 8 | 9 
                |       |
            {board[6]}   |   {board[7]}   |   {board[8]}
                |       |

        """
        )


def main():
    # game board
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player = ""
    symbol = ""

    #pequena intro
    time.sleep(0.8)
    for n in range(1,4):
        print("Loading","." * n)
        time.sleep(0.5)

    print("\n> Player1 is X and PLayer2 is O!")
    time.sleep(2)

    # actual game
    for i in range(1, 10):
        # Decision of turn
        player, symbol = choosePlayer(i)
        
        # print of the board
        printBoard(player, board)

        # play per iteration
        while True:
            try:
                play = int(input("Space (1-9): "))
            except:
                print("Invalid input! Try again.")
                continue

            if board[play - 1] == " ":
                board[play - 1] = symbol
                break
            print("Invalid play! Try again.")

        # win condition (checks if player made a winning move, each play)
        if checkColumn(board, symbol) or checkRow(board, symbol) or checkDiagonal(board, symbol):
            printBoard(player, board)   # print the board again to show the play
            print(f"\nThe winner is {player}\n")
            time.sleep(1)
            exit(0)
    
    # if 9 moves were made (board completelly filled) a draw is issued
    printBoard(player, board)   # print the board again to show the play
    print("It's a Draw!")
            
        
if __name__ == '__main__':
    main()