import pygame as pg, math, time

WIDTH, HEIGHT = 500, 500
FPS = 60
class Clock(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.hr, self.mr, self.sr = 150, 200, 200

    def update(self):
        self.image.fill((0, 0, 0, 0))
        s = time.localtime().tm_sec
        m = time.localtime().tm_min
        h = time.localtime().tm_hour % 12
        hdir = h*30-90
        mdir = m*6-90
        sdir = s*6-90
        hx = WIDTH/2+self.hr*math.cos(math.radians(hdir))
        hy = HEIGHT/2+self.hr*math.sin(math.radians(hdir))
        pg.draw.line(self.image, (0,0,0),
                    (WIDTH/2,HEIGHT/2),
                    (hx,hy),6)
        hx = WIDTH/2+self.mr*math.cos(math.radians(mdir))
        hy = HEIGHT/2+self.mr*math.sin(math.radians(mdir))
        pg.draw.line(self.image, (0,0,0),
                    (WIDTH/2,HEIGHT/2),
                    (hx,hy),4)
        hx = WIDTH/2+self.sr*math.cos(math.radians(sdir))
        hy = HEIGHT/2+self.sr*math.sin(math.radians(sdir))
        pg.draw.line(self.image, (0,0,0),
                    (WIDTH/2,HEIGHT/2),
                    (hx,hy),2)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('アナログ時計')
clock = pg.time.Clock()

all_circles = pg.sprite.Group()
all_circles.add(Clock())

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_circles.update()
    screen.fill(pg.Color('white'))
    all_circles.draw(screen)

    pg.display.update()
    clock.tick(FPS)

pg.quit()
