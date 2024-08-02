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
    score = evaluate(board, variables.win_list)

    if score == 10:
        return score

    if score == -10:
        return score

    if functions.draw_game(board):
        return 0

    if isMax:
        best = -1000
        for i, j in enumerate(board):
            if j == False:
                board[i] = "X"
                best = max(best, minimax(board, depth + 1, not isMax, alpha, beta))
                board[i] = False
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = 1000
        for i, j in enumerate(board):
            if j == False:
                board[i] = "O"
                best = min(best, minimax(board, depth + 1, not isMax, alpha, beta))
                board[i] = False
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best


def findBestMove(board):
    bestVal = -1000
    bestMove = -1

    for i, j in enumerate(board):
        if j == False:
            board[i] = "X"
            moveVal = minimax(board, 0, False, -1000, 1000)
            board[i] = False

            if moveVal > bestVal:
                bestMove = i
                bestVal = moveVal


    return bestMove

