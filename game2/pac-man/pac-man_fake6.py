import pygame as pg
import sys,random

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
        self.rect = self._images[1].get_rect()
        self.play_end = False
        self.play_clear = False

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

class Snack:
    def __init__(self):
        self._x = random.randint(5,WIDTH-5)
        self._y = random.randint(5,HEIGHT-5)
        self._display = True

class Monster:
    def __init__(self):
        self._images = [
            pg.image.load("images/monster0.png"),
            pg.image.load("images/monster1.png")
        ]
        self._x = WIDTH
        self._y = random.randint(15,HEIGHT-15)
        self._speed = 3

    def move(self,pac_man):
        if self._x < pac_man._x:
            self._x += self._speed
        if self._x > pac_man._x:
            self._x -= self._speed
        if self._y < pac_man._y:
            self._y += self._speed
        if self._y > pac_man._y:
            self._y -= self._speed

    def draw(self,screen,mode):
        img = self._images[mode%2]
        self.rect = img.get_rect(center=(self._x,self._y))
        screen.blit(img,self.rect)

def main():
    pg.init()
    pg.display.set_caption("パックマンもどき")
    screen = pg.display.set_mode(WINDOW_SIZE)
    clock = pg.time.Clock()
    tmr = 0
    pac_man = Pac_man()
    snacks = [Snack() for i in range(50)]
    monster = Monster()
    over,clear = False,False
    sound_end = pg.mixer.Sound('sounds/pac-man_end.mp3')
    sound_eat = pg.mixer.Sound('sounds/pac-man_eat.mp3')
    sound_clear = pg.mixer.Sound('sounds/pac-man_clear.mp3')

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
        for s in snacks:
            if s._display:
                s.rect = pg.draw.circle(screen,(255,255,0),(s._x,s._y),5,width=0)
                if pg.sprite.collide_circle(pac_man,s):
                    sound_eat.play()
                    s._display = False

        if not over and not clear:
            pac_man.move()
            monster.move(pac_man)
        pac_man.draw(screen,tmr//10)
        monster.draw(screen,tmr//10)

        if over:
            if not pac_man.play_end:
                sound_end.play()
                pac_man.play_end = True
            font = pg.font.SysFont('helvetica', 30)
            txt = font.render('GAME OVER',True,(255,255,255))
            screen.blit(txt,((WIDTH-txt.get_width())/2,(HEIGHT-txt.get_height())/2))
        if clear:
            if not pac_man.play_clear:
                sound_clear.play()
                pac_man.play_clear = True
            font = pg.font.SysFont('helvetica', 30)
            txt = font.render('GAME CLEAR',True,(255,255,255))
            screen.blit(txt,((WIDTH-txt.get_width())/2,(HEIGHT-txt.get_height())/2))

        if pg.sprite.collide_circle(pac_man,monster):
            over = True
        count = 0
        for s in snacks:
            if not s._display:
                count += 1
        if count >= 50:
            clear = True

        pg.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
