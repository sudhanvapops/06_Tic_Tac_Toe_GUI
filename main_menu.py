import pygame
import Button_Class


Single_player_image = pygame.image.load("S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/Single Player.png")
Two_player_image = pygame.image.load("S:/Exp/00_Projects/Python_Projects/06_Tic_Tac_Toe_GUI/assets/Two Player.png")


Single_player_button = Button_Class.Button(200,140,Single_player_image)
Two_player_button = Button_Class.Button(200,240,Two_player_image)


def main_menu(screen):

    screen.fill("#FF4B91")
    
    for events in pygame.event.get():

        if events.type == pygame.QUIT:
            pygame.quit()
            exit()

    action_1 = Single_player_button.draw(screen)
    action_2 = Two_player_button.draw(screen)

    pygame.display.update()


    return action_1,action_2
