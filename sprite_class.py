import pygame

class Sprite:
    def __init__(self, image_obj,x,y):
        self.image = image_obj
        self.rect = self.image.get_rect(center=(y,x))

    def draw_(self,surface):
        surface.blit(self.image, self.rect)