import pygame

# Constants

COLOR = "#FAFFAF"

# Variables

# Clock
clock = pygame.time.Clock()

# X and O States
XO_State = [False,False,False,False,False,False,False,False,False]
XO_Object_State =[False,False,False,False,False,False,False,False,False]

# Visited array
visited_spots = []

# Available array
available_spots = [0,1,2,3,4,5,6,7,8]

# x,y 
x,y = False,False

# Turn Variable
Turn = True

# game state
game_over = False
game_state = "main_menu"

# winning line
wining_line = ()
win_text = ""
Draw = False

# Winlist 
win_list = [
    [0, 1, 2],  # first row
    [3, 4, 5],  # second row
    [6, 7, 8],  # third row
    [0, 3, 6],  # first column
    [1, 4, 7],  # second column
    [2, 5, 8],  # third column
    [0, 4, 8],  # diagonal
    [2, 4, 6]   # diagonal
]


# Index Dictionary 

index_dic = {
    (0,0) : 0,
    (0,1) : 1,
    (0,2) : 2,
    (1,0) : 3,
    (1,1) : 4,
    (1,2) : 5,
    (2,0) : 6,
    (2,1) : 7,
    (2,2) : 8,
}


# Images 

# Board
Board = pygame.image.load("S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/Board.png").convert_alpha()

# X and O

X_Image = pygame.image.load("S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/X.png").convert_alpha()
O_Image = pygame.image.load("S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/O.png").convert_alpha()

X_Win_Image = pygame.image.load("S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/Winning X.png").convert_alpha()
O_Win_Image = pygame.image.load("S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/Winning O.png").convert_alpha()


# Rectangles

# Board_Rect
Board_Rect = Board.get_rect(center=(200,200))