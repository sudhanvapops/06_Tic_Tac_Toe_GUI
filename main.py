import pygame
from sys import exit
import sprite_class

# Functions

# Function to change the array X and O State
def change_X(x_state,x:int,y:int):

    global Turn,game_over,screen,win_text,Draw
    # Implement logic for array change here
    try :
        if  x_state[x][y] == False:

            if Turn == True:
                x_state[x][y] = "X"
            elif Turn == False:
                x_state[x][y] = "O"

            change_O(O_State,x,y)

            if check_win():
                Turn = not Turn
                game_over = True
                return
            elif draw_game() == True:
                win_text = "Draw"
                game_over = True
                Draw = True
                return
            Turn = not Turn
            return
        
        else:
            pass
        
    except IndexError :
        pass



# Function to draw X and O
def change_O(o_state,x,y):

    x_ = ((x + 1)*100)
    y_ = ((y + 1)*100)

    try :
        if Turn == True and o_state[x][y] == False:
            obj = sprite_class.Sprite(X_Image,x_,y_)
            o_state[x][y]=obj
        elif Turn == False  and o_state[x][y] == False:
            obj = sprite_class.Sprite(O_Image,x_,y_)
            o_state[x][y]=obj
    except IndexError :
        pass
    



def draw_board(o_state):
    for x in range(len(o_state)):
        for y in range(len(o_state[x])):
            if o_state[x][y] != False:
                o_state[x][y].draw_(screen)


def check_win():

        global Turn,game_over,wining_line,win_text,X_Win_Image


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
            if Turn == True:
                if X_State[row[0][0]][row[0][1]] == X_State[row[1][0]][row[1][1]] == X_State[row[2][0]][row[2][1]] == "X":

                    start = O_State[row[0][0]][row[0][1]].rect.center   
                    end = O_State[row[2][0]][row[2][1]].rect.center 

                    O_State[row[0][0]][row[0][1]].image = X_Win_Image
                    O_State[row[1][0]][row[1][1]].image = X_Win_Image
                    O_State[row[2][0]][row[2][1]].image = X_Win_Image

                    wining_line = (start, end)
                    win_text = "X wins"

                    return True
            else:
                if X_State[row[0][0]][row[0][1]] == X_State[row[1][0]][row[1][1]] == X_State[row[2][0]][row[2][1]] == "O":

                    start = O_State[row[0][0]][row[0][1]].rect.center   
                    end = O_State[row[2][0]][row[2][1]].rect.center 

                    O_State[row[0][0]][row[0][1]].image = O_Win_Image
                    O_State[row[1][0]][row[1][1]].image = O_Win_Image
                    O_State[row[2][0]][row[2][1]].image = O_Win_Image

                    wining_line = (start, end)
                    win_text = "O wins"
                    return True
                
        return False



# Game Draw Function
def draw_game():
    for row in X_State:
        for col in row:
            if col == False:
                return False
    
    return True


def draw_line(surface,start,end,width=9):

    pygame.draw.line(surface,"Black",start,end,width)
    return


def draw_text(surface,text_):
    font = pygame.font.Font('S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/Roboto-Regular.ttf', 32)

    text = font.render(text_, True,"Black")
    textRect = text.get_rect(center = (200,20))
    surface.blit(text,textRect)

    text_2 = font.render("Press R to Restart", True,"Black")
    text_2_rect = text_2.get_rect(center = (200,380))
    surface.blit(text_2,text_2_rect)




pygame.init()

icon = pygame.image.load("S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/tic-tac-toe.png")

pygame.display.set_icon(icon)
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe!")
clock = pygame.time.Clock()

# Constants

COLOR = "#FAFFAF"

# Variables

# X and O States
X_State = [[False,False,False],[False,False,False],[False,False,False]]
O_State = [[False,False,False],[False,False,False],[False,False,False]]


x,y = False,False

# Turn Variable
Turn = True

# game state
game_over = False

# winning line
wining_line = ()
win_text = ""
Draw = False

# Images 

# Board
Board = pygame.image.load("S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/Board.png").convert_alpha()

# X and O

X_Image = pygame.image.load("S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/X.png").convert_alpha()
O_Image = pygame.image.load("S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/O.png").convert_alpha()

X_Win_Image = pygame.image.load("S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/Winning X.png").convert_alpha()
O_Win_Image = pygame.image.load("S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/Winning O.png").convert_alpha()


# Sprites

# Rectangles

# Board_Rect
Board_Rect = Board.get_rect(center=(200,200))


def game_play(screen): 

    global O_State,X_State,game_over,Draw,Turn

    while True:

        screen.fill(COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == True and game_over == False:

                # To ge Mouse Position
                mouse_pos = pygame.mouse.get_pos()

                # X is Row , Y is Column  returns tupule of index (x,y)
                x = round((mouse_pos[1] / 100)  )  - 1
                y = round((mouse_pos[0] / 100)  )  - 1

                change_X(X_State,x,y)

            # For Restart Game
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_r):
                game_over = False
                Turn = True
                Draw = False
                X_State = [[False,False,False],[False,False,False],[False,False,False]]
                O_State = [[False,False,False],[False,False,False],[False,False,False]]


        screen.blit(Board,Board_Rect)
        draw_board(O_State)
        if game_over == True:
            if Draw == True:
                draw_text(screen,win_text)
            else:
                draw_text(screen,win_text)
                draw_line(screen,wining_line[0],wining_line[1])

        pygame.display.update()
        clock.tick(60)


game_play(screen)