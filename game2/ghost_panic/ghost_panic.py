import sys
import pygame
from settings import Settings
from ghost import Ghost
from player import Player

class GhostPanic:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("ゴーストパニック")

        self.font = pygame.font.Font(None, 80)
        self.timer = 0
        self.counter = 0

        self.ghost = Ghost(self)
        self.player = Player(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

            if not self.settings.hitflag:
                self.ghost.update()
                self.player.update()
                self.counter += 1
                if self.counter % 100 == 0:
                    self.timer += 1
            if pygame.sprite.collide_rect(self.ghost, self.player):
                self.settings.hitflag = True
                self.screen.fill(self.settings.go_color)
            else:
                self.screen.fill(self.settings.bg_color)
            self.screen.blit(self.ghost.image, self.ghost.rect)
            self.screen.blit(self.player.image, self.player.rect)

            self.text = self.font.render(str(self.timer), True, (0,0,0))
            self.screen.blit(self.text, [300, 50])

#            pygame.display.flip()
            pygame.display.update()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False
        elif event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False

if __name__ == '__main__':
    gp = GhostPanic()
    gp.run_game()
