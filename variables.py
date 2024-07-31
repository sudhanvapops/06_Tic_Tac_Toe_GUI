import pygame

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
game_state = "main_menu"

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


# Rectangles

# Board_Rect
Board_Rect = Board.get_rect(center=(200,200))