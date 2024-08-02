import functions
import variables


def evaluation_function(XO_State,win_list,Turn):

    player = "X" if Turn else "O"

    for row in win_list:
        if XO_State[row[0]] == XO_State[row[1]] == XO_State[row[2]] == player:
            return 10
        else:
            return -10
    
    return 0

def minimax(XO_State,depth, isMax):
    
    score = evaluation_function(variables.XO_State,variables.win_list,variables.Turn)

    if score == 10:
        return score
    
    if score == -10:
        return score
    
    if (functions.draw_game(variables.XO_State) == True):
        return 0
    
    # If maximizer move
    if (isMax):
        best = float("-inf")

        # Traversing all the cells
        for i,j in enumerate(XO_State):

            if j == False:

                XO_State[i] = "X"

                best = max(best, minimax(XO_State,depth+1,(not isMax))) 

                # Undoing the move
                XO_State[i] = False
        
        return best
    
    elif (isMax == False):

        best = float("inf")
        
        for i,j in enumerate(XO_State):

            if j == False:

                XO_State[i] = "O"

                best = min(best, minimax(XO_State,depth+1,(not isMax))) 

                # Undoing the move
                XO_State[i] = False

        return best


def find_best_move(XO_State,Turn):

    best_val = float("-inf")
    bestMove = -1
    player = "X" if Turn else "O"


    for i,j in enumerate(XO_State):

        if j == False:

            XO_State[i] = player

            #  compute evaluation function for this move
            move_value = minimax(XO_State,0,Turn)

            XO_State[i] = False

            # If the value of the current move is  more than the best value, then update  best/ 
            if (move_value > best_val) :                 
                    bestMove = i 
                    best_val = move_value

    return bestMove