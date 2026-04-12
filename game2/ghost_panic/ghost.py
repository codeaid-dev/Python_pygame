import pygame

class Ghost:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('images/ghost.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.rect.right > self.screen_rect.right or self.rect.left < 0:
            self.settings.ghost_xspeed *= -1
        if self.rect.bottom > self.screen_rect.bottom or self.rect.top < 0:
            self.settings.ghost_yspeed *= -1

        self.x += self.settings.ghost_xspeed
        self.y += self.settings.ghost_yspeed
        self.rect.x = self.x
        self.rect.y = self.y
