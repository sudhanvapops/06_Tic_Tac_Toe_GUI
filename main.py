import pygame
import main_menu

pygame.init()

icon = pygame.image.load("S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/tic-tac-toe.png")

pygame.display.set_icon(icon)
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe!")


import variables
import two_p_game


while True:

    if variables.game_state == "main_menu":

        action_1,action_2 = main_menu.main_menu(screen)

        if action_1:
            pass
        elif action_2:
            variables.game_state = "2pgame"

    elif variables.game_state == "1pgame":
        pass

    elif variables.game_state == "2pgame":
        two_p_game.two_p_main_game(screen)


    pygame.display.update()
    variables.clock.tick(60)

