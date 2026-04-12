import pygame as pg
import sys

WINDOW_SIZE = WIDTH,HEIGHT = 800,450
BACKGROUND = (0,0,0)
FPS = 60

class Pac_man:
    def __init__(self):
        self._images = [
            pg.image.load("images/pac-man0.png"),
            pg.image.load("images/pac-man1.png")
        ]
        self._x = WIDTH/2
        self._y = HEIGHT/2
        self._speed = 5
        self._dir = 1

    def move(self):
        key = pg.key.get_pressed()
        if key[pg.K_UP]:
            self._y -= self._speed
            self._dir = 4
        if key[pg.K_DOWN]:
            self._y += self._speed
            self._dir = 2
        if key[pg.K_RIGHT]:
            self._x += self._speed
            self._dir = 1
        if key[pg.K_LEFT]:
            self._x -= self._speed
            self._dir = 3

        if self._x<-15:
            self._x = WIDTH+15
        if self._x>WIDTH+15:
            self._x = -15
        if self._y<-15:
            self._y = HEIGHT+15
        if self._y>HEIGHT+15:
            self._y = -15

    def draw(self,screen,mode):
        img = self._images[mode%2]
        if self._dir == 1: #RIGHT
            rotated = pg.transform.rotate(img, 0)
        if self._dir == 4: #UP
            rotated = pg.transform.rotate(img, 90)
        if self._dir == 3: #LEFT
            rotated = pg.transform.rotate(img, 180)
        if self._dir == 2: #DOWN
            rotated = pg.transform.rotate(img, 270)
        self.rect = rotated.get_rect(
            center=img.get_rect(center=(self._x, self._y)).center)
        screen.blit(rotated,self.rect)

def main():
    pg.init()
    pg.display.set_caption("パックマンもどき")
    screen = pg.display.set_mode(WINDOW_SIZE)
    clock = pg.time.Clock()
    tmr = 0
    pac_man = Pac_man()

    while True:
        tmr += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F1:
                    screen = pg.display.set_mode(WINDOW_SIZE, pg.FULLSCREEN)
                if event.key == pg.K_F2 or event.key == pg.K_ESCAPE:
                    screen = pg.display.set_mode(WINDOW_SIZE)

        screen.fill(BACKGROUND)
        pac_man.move()
        pac_man.draw(screen,tmr//10)
        pg.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
