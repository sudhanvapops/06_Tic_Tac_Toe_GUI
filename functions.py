import pygame
import sprite_class
import variables


# Converts 2d index to 1d index
def convert_2Dindex_to_1Dindex(x,y) -> int:
    index = variables.index_dic[(x,y)] if (x,y) in variables.index_dic else None
    return index


# Function to Check Win 
def check_win(XO_State, XO_Object_State,win_list):

    player = "X" if variables.Turn else "O"
    win_image = variables.X_Win_Image if player == "X" else variables.O_Win_Image

    for row in win_list:
        if XO_State[row[0]] == XO_State[row[1]] == XO_State[row[2]] == player:
            start = XO_Object_State[row[0]].rect.center
            end = XO_Object_State[row[2]].rect.center

            for index in row:
                XO_Object_State[index].image = win_image

            variables.wining_line = (start, end)
            variables.win_text = f"{player} wins"
            return True

    return False


# Entry point
# Function to change the array X and O State
def change_XO_State(XO_State,index_1D,x,y):

    # Implement logic for array change here
    try :
        if (index_1D != None) and (0 <= index_1D <= 9 ):

            if  XO_State[index_1D] == False:

                variables.available_spots.remove(index_1D)
                variables.visited_spots.append(index_1D)

                XO_State[index_1D] = "X" if variables.Turn == True else "O"
                
                if variables.Turn != True:
                    for key,value in variables.index_dic.items():
                        if index_1D == value:
                            x = key[0] 
                            y = key[1]

                Change_XO_object_State(variables.XO_Object_State,index_1D,variables.Turn,x,y)


                if check_win(variables.XO_State,variables.XO_Object_State,variables.win_list):
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
def Change_XO_object_State(XO_Object_State,index_1d,Turn,x,y):


    # y = mx + c 
    # m = 100,  x = (x + 1)

    x_ = ((x + 1)*100)
    y_ = ((y + 1)*100)


    try :
        if XO_Object_State[index_1d] == False:

            if Turn == True:
                obj = sprite_class.Sprite(variables.X_Image,x_,y_)

            elif Turn == False:
                obj = sprite_class.Sprite(variables.O_Image,x_,y_)

            XO_Object_State[index_1d] = obj
        
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
    variables.visited_spots = []
    variables.available_spots = [0,1,2,3,4,5,6,7,8]


def handle_click():
    if pygame.mouse.get_pressed()[0] == True and variables.game_over == False:

        # To ge Mouse Position
        mouse_pos = pygame.mouse.get_pos()

        # X is Row , Y is Column  returns tupule of index (x,y)
        x = round((mouse_pos[1] / 100)  )  - 1
        y = round((mouse_pos[0] / 100)  )  - 1

        # Entrypoint
        index_1D = convert_2Dindex_to_1Dindex(x,y)
        change_XO_State(variables.XO_State,index_1D,x,y)