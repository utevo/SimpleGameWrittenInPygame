import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, bullet_settings, ship):

        self.__bullet_settings = bullet_settings

        image_path = self.__bullet_settings.image_path
        self.image = pygame.image.load(image_path)

        image_resolution = self.__bullet_settings.image_resolution
        self.image = pygame.transform.scale(self.image, 
            image_resolution)

        self.rect = self.image.get_rect()
        self.__ship_rect = ship.rect

        self.rect.centerx = self.__ship_rect.centerx
        self.rect.top = self.__ship_rect.top

        self.__centery = float(self.rect.centery)

    def update(self):
        self.__centery -= self.__bullet_settings.speed_factor
        self.rect.centery = self.__centery

    def draw(self, screen_surface):
        screen_surface.blit(self.image, self.rect)

