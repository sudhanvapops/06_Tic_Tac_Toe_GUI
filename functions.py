import pygame
import sprite_class
import variables


# Function to change the array X and O State
def change_X(x_state,x:int,y:int):

    # Implement logic for array change here
    try :
        if  x_state[x][y] == False:

            if variables.Turn == True:
                x_state[x][y] = "X"
            elif variables.Turn == False:
                x_state[x][y] = "O"

            change_O(variables.O_State,x,y,variables.Turn)

            if check_win(variables.X_State,variables.O_State):
                variables.Turn = not variables.Turn
                variables.game_over = True
                return
            elif draw_game(variables.X_State) == True:
                variables.win_text = "Draw"
                variables.game_over = True
                variables.Draw = True
                return
            variables.Turn = not variables.Turn
            return
        
        else:
            pass
        
    except IndexError :
        pass


# Function to Check Win 
def check_win(X_State,O_State):


        win_list = [
            [(0, 0), (0, 1), (0, 2)],  # first row
            [(1, 0), (1, 1), (1, 2)],  # second row
            [(2, 0), (2, 1), (2, 2)],  # third row
            [(0, 0), (1, 0), (2, 0)],  # first column
            [(0, 1), (1, 1), (2, 1)],  # second column
            [(0, 2), (1, 2), (2, 2)],  # third column
            [(0, 0), (1, 1), (2, 2)],  # diagonal
            [(0, 2), (1, 1), (2, 0)]   # diagonal
        ]
        
        for row in win_list:
            if variables.Turn == True:
                if X_State[row[0][0]][row[0][1]] == X_State[row[1][0]][row[1][1]] == X_State[row[2][0]][row[2][1]] == "X":

                    start = O_State[row[0][0]][row[0][1]].rect.center   
                    end = O_State[row[2][0]][row[2][1]].rect.center 

                    O_State[row[0][0]][row[0][1]].image = variables.X_Win_Image
                    O_State[row[1][0]][row[1][1]].image = variables.X_Win_Image
                    O_State[row[2][0]][row[2][1]].image = variables.X_Win_Image

                    variables.wining_line = (start, end)
                    variables.win_text = "X wins"
                    return True
            else:
                if X_State[row[0][0]][row[0][1]] == X_State[row[1][0]][row[1][1]] == X_State[row[2][0]][row[2][1]] == "O":

                    start = O_State[row[0][0]][row[0][1]].rect.center   
                    end = O_State[row[2][0]][row[2][1]].rect.center 

                    O_State[row[0][0]][row[0][1]].image = variables.O_Win_Image
                    O_State[row[1][0]][row[1][1]].image = variables.O_Win_Image
                    O_State[row[2][0]][row[2][1]].image = variables.O_Win_Image

                    variables.wining_line = (start, end)
                    variables.win_text = "O wins"
                    return True
                
        return False


# Function to draw X and O on the screen when mouse is clicked on the position
def change_O(o_state,x,y,Turn):


    # y = mx + c 
    # m = 100,  x = (x + 1)

    x_ = ((x + 1)*100)
    y_ = ((y + 1)*100)

    try :
        if Turn == True and o_state[x][y] == False:
            obj = sprite_class.Sprite(variables.X_Image,x_,y_)
            o_state[x][y]=obj
        elif Turn == False  and o_state[x][y] == False:
            obj = sprite_class.Sprite(variables.O_Image,x_,y_)
            o_state[x][y]=obj
    except IndexError :
        pass
    



# FUnction to draw Board on the screen
def draw_board(o_state,screen):
    for x in range(len(o_state)):
        for y in range(len(o_state[x])):
            if o_state[x][y] != False:
                o_state[x][y].draw_(screen)

# Game Draw Function
def draw_game(X_State):
    for row in X_State:
        for col in row:
            if col == False:
                return False
    
    return True


# TO draw Lines
def draw_line(surface,start,end,width=9):

    pygame.draw.line(surface,"Black",start,end,width)
    return


# To draw Text
def draw_text(surface,text_):
    font = pygame.font.Font('S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/Roboto-Regular.ttf', 32)

    text = font.render(text_, True,"Black")
    textRect = text.get_rect(center = (200,20))
    surface.blit(text,textRect)

    text_2 = font.render("Press R to Restart", True,"Black")
    text_2_rect = text_2.get_rect(center = (200,380))
    surface.blit(text_2,text_2_rect)

def rest_game():
    variables.game_over = False
    variables.Turn = True
    variables.Draw = False
    variables.wining_line = ()
    variables.X_State = [[False,False,False],[False,False,False],[False,False,False]]
    variables.O_State = [[False,False,False],[False,False,False],[False,False,False]]