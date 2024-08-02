import pygame
import variables
import functions
import one_p_functions


def one_p_main_game(screen):
    
    while True:    

        screen.fill(variables.COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # For O Turn
            if variables.Turn == True:
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == True and variables.game_over == False:

                    # To ge Mouse Position
                    mouse_pos = pygame.mouse.get_pos()

                    # X is Row , Y is Column  returns tupule of index (x,y)
                    x = round((mouse_pos[1] / 100)  )  - 1
                    y = round((mouse_pos[0] / 100)  )  - 1

                    # Entrypoint
                    index_1D = functions.convert_2Dindex_to_1Dindex(x,y) 
                    functions.change_XO_State(variables.XO_State,index_1D,x,y)
    
            elif variables.Turn == False:
                    
                # Entrypoint
                best_move = one_p_functions.find_best_move(variables.XO_State,variables.Turn)
                print(f"{best_move = }")
                functions.change_XO_State(variables.XO_State,best_move,0,0)


            # For Restart Game
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_r):
                functions.rest_game()

            # For Going Back
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_b):
                functions.rest_game()
                variables.game_state = "main_menu"
                return


        screen.blit(variables.Board,variables.Board_Rect)
        
        functions.draw_board(variables.XO_Object_State,screen)

        if variables.game_over == True:
            functions.draw_text(screen,variables.win_text)
            if variables.Draw != True:
                functions.draw_line(screen,variables.wining_line[0],variables.wining_line[1])
        
        pygame.display.update()
        variables.clock.tick(60)
