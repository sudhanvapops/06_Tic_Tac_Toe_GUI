import pygame

class Button():
    def __init__(self, x, y, image, scale=1):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(self.image)  # Create mask from the button image
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        # Check mouse clicked and mouse hover
        if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
            # Check for collision with pixel-perfect detection
            if self.rect.collidepoint(pos):
                mouse_x, mouse_y = pos
                mouse_pos = (mouse_x - self.rect.left, mouse_y - self.rect.top)
                if 0 <= mouse_pos[0] < self.mask.get_size()[0] and 0 <= mouse_pos[1] < self.mask.get_size()[1]:
                    if self.mask.get_at(mouse_pos):
                        self.clicked = True
                        action = True

        if pygame.mouse.get_pressed()[0] == 0 and self.clicked:
            self.clicked = False

        surface.blit(self.image, self.rect)

        return action
