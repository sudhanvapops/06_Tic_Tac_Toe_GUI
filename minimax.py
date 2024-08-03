import functions
import variables

player = variables.Turn

def evaluate(board, winlist):
    # Checking for Rows for X or O victory.
    for row in winlist:
        if board[row[0]] == board[row[1]] == board[row[2]] == "X":
            return 10
        elif board[row[0]] == board[row[1]] == board[row[2]] == "O":
            return -10

    return 0


# This is the minimax function with Alpha-Beta pruning.
def minimax(board, depth, isMax, alpha, beta):

    # Evaluates the minimax function
    score = evaluate(board, variables.win_list)

    if score == 10:
        return score

    if score == -10:
        return score

    if functions.draw_game(board) == True:
        return 0

    if isMax:

        best = -1000

        # Itrates thriugh all the blank spaces 
        for i, j in enumerate(board):

            if j == False:

                board[i] = "X"
                eval = minimax(board, depth + 1, not isMax, alpha, beta)
                best = max(best, eval )

                # Undoing the move
                board[i] = False

                alpha = max(alpha, eval)
                if beta <= alpha:
                    break

        return best
    
    else:
        best = 1000
        for i, j in enumerate(board):

            if j == False:

                board[i] = "O"
                eval =  minimax(board, depth + 1, not isMax, alpha, beta)
                best = min(best, eval)
                board[i] = False

                beta = min(beta, eval)
                if beta <= alpha:
                    break

        return best


def findBestMove(board):

    bestVal = -1000
    bestMove = -1

    for i, j in enumerate(board):
        
        if j == False:

            # Change here for "O" 
            # Puts First MOve X So next move is False
            board[i] = "X"
            # And here in False
            moveVal = minimax(board, 0, False, -1000, 1000)
            board[i] = False

            if moveVal > bestVal:
                bestMove = i
                bestVal = moveVal

    return bestMove,bestVal

