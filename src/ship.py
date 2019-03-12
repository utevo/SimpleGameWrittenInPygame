import pygame

class Ship():

    def __init__(self, ship_settings, screen):
        self.screen_surface = screen.surface

        self.ship_settings = ship_settings

        image_path = self.ship_settings.image_path
        self.image = pygame.image.load(image_path)

        self.image_resolution = self.ship_settings.image_resolution
        self.image = pygame.transform.scale(self.image, 
            self.image_resolution)

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen_surface.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.__centerx = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.__centerx += self.ship_settings.speed_factor

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.__centerx -= self.ship_settings.speed_factor

        self.rect.centerx = self.__centerx

    def draw(self):
        self.screen_surface.blit(self.image, self.rect)