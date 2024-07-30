import pygame

# Class
class Button():
    def __init__(self, x, y, image, scale=1):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        # self.mask_image = pygame.mask.from_surface(self.image)
        self.rect.center = (x,y)
        self.clicked = False
    
    def draw(self,surface):
        action = False
        pos = pygame.mouse.get_pos()

        # Check mouse clicked and mouse hover
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            # check for colllison
            if self.rect.collidepoint(pos):
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
            self.clicked = False

        surface.blit(self.image, self.rect)

        return action
    