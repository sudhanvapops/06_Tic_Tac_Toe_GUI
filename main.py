import pygame
from sys import exit
import main_menu


pygame.init()

icon = pygame.image.load("S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/tic-tac-toe.png")

pygame.display.set_icon(icon)
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe!")
clock = pygame.time.Clock()


import variables
import functions


# Functions

def game_play(screen): 


    while True:
        if variables.game_state == "main_menu":
            action_1,action_2 = main_menu.main_game(screen)
            if action_2:
                variables.game_state = "2pgame"
        
        elif variables.game_state == "2pgame":

            screen.fill(variables.COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == True and variables.game_over == False:

                    # To ge Mouse Position
                    mouse_pos = pygame.mouse.get_pos()

                    # X is Row , Y is Column  returns tupule of index (x,y)
                    x = round((mouse_pos[1] / 100)  )  - 1
                    y = round((mouse_pos[0] / 100)  )  - 1

                    functions.change_XO_State(variables.XO_State,x,y)

                # For Restart Game
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_r):
                    functions.rest_game()

                if (event.type == pygame.KEYDOWN and event.key == pygame.K_b):
                    functions.rest_game()
                    variables.game_state = "main_menu"


            screen.blit(variables.Board,variables.Board_Rect)
            functions.draw_board(variables.XO_Object_State,screen)
            if variables.game_over == True:
                functions.draw_text(screen,variables.win_text)
                if variables.Draw != True:
                    functions.draw_line(screen,variables.wining_line[0],variables.wining_line[1])

            pygame.display.update()

        clock.tick(60)

game_play(screen)