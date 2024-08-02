import pygame
import sprite_class
import variables


# Function to Check Win 
def check_win(XO_State,XO_Object_State):


        win_list = [
            [0,1,2],  # first row
            [3,4,5],  # second row
            [6,7,8],  # third row
            [0,3,6],  # first column
            [1,4,7],  # second column
            [2,5,8],  # third column
            [0,4,8],  # diagonal
            [2,4,6]   # diagonal
        ]
        
        for row in win_list:
            if variables.Turn == True:
                if XO_State[row[0]] == XO_State[row[1]] == XO_State[row[2]] == "X":

                    start = XO_Object_State[row[0]].rect.center   
                    end   = XO_Object_State[row[2]].rect.center 

                    XO_Object_State[row[0]].image = variables.X_Win_Image
                    XO_Object_State[row[1]].image = variables.X_Win_Image
                    XO_Object_State[row[2]].image = variables.X_Win_Image

                    variables.wining_line = (start, end)
                    variables.win_text = "X wins"
                    return True
            else:
                if XO_State[row[0]] == XO_State[row[1]] == XO_State[row[2]] ==  "O":

                    start = XO_Object_State[row[0]].rect.center   
                    end   = XO_Object_State[row[2]].rect.center 

                    XO_Object_State[row[0]].image = variables.O_Win_Image
                    XO_Object_State[row[1]].image = variables.O_Win_Image
                    XO_Object_State[row[2]].image = variables.O_Win_Image

                    variables.wining_line = (start, end)
                    variables.win_text = "O wins"
                    return True
                
        return False


# Converts 2d index to 1d index
def convert_2Dindex_to_1Dindex(x,y) -> int:

    index = variables.index_dic[(x,y)] if (x,y) in variables.index_dic else ""

    if index != "":
        return  index 
    
    return None


# Function to change the array X and O State
def change_XO_State(XO_State,x:int,y:int):

    # Implement logic for array change here
    try :

        index_1D = convert_2Dindex_to_1Dindex(x,y) 

        if index_1D != None:
            if  XO_State[index_1D]== False:

                if variables.Turn == True:
                    XO_State[index_1D]= "X"
                elif variables.Turn == False:
                    XO_State[index_1D]= "O"

                Change_XO_object_State(variables.XO_Object_State,x,y,variables.Turn)

                if check_win(variables.XO_State,variables.XO_Object_State):
                    variables.Turn = not variables.Turn
                    variables.game_over = True
                    return
                elif draw_game(variables.XO_State) == True:
                    variables.win_text = "Draw"
                    variables.game_over = True
                    variables.Draw = True
                    return
                variables.Turn = not variables.Turn
                return
            
    except IndexError :
        pass



# Function to draw X and O on the screen when mouse is clicked on the position
def Change_XO_object_State(XO_Object_State,x,y,Turn):


    # y = mx + c 
    # m = 100,  x = (x + 1)

    x_ = ((x + 1)*100)
    y_ = ((y + 1)*100)

    index_1d = convert_2Dindex_to_1Dindex(x,y)

    try :
        if Turn == True and XO_Object_State[index_1d] == False:
            obj = sprite_class.Sprite(variables.X_Image,x_,y_)
            XO_Object_State[index_1d]=obj
        elif Turn == False  and XO_Object_State[index_1d] == False:
            obj = sprite_class.Sprite(variables.O_Image,x_,y_)
            XO_Object_State[index_1d]=obj
    except IndexError :
        pass
    



# FUnction to draw Board on the screen
def draw_board(XO_Object_State,screen):

    for xo_object in XO_Object_State:
        if xo_object != False:
            xo_object.draw_(screen)

# Game Draw Function
def draw_game(XO_State):
    for col in XO_State:
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
    variables.XO_State = [False,False,False,False,False,False,False,False,False]
    variables.XO_Object_State = [False,False,False,False,False,False,False,False,False]