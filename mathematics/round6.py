import pygame as pg, math

WIDTH, HEIGHT = 500, 500
FPS = 60
class Planet(pg.sprite.Sprite):
    def __init__(self, up):
        super().__init__()
        self.image = pg.Surface((200, 200), pg.SRCALPHA)
        pg.draw.circle(self.image, (255,150,0), (100, 100), 100,
                       draw_top_left=up,draw_top_right=up,
                       draw_bottom_left=not up,draw_bottom_right=not up)
        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT/2))

class Satellite(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((20, 20), pg.SRCALPHA)
        pg.draw.circle(self.image, (0,255,255), (10, 10), 10)
        self.rw = 200
        self.rh = 50
        x = WIDTH/2+self.rw*math.cos(0)
        y = HEIGHT/2+self.rh*math.sin(0)
        self.rect = self.image.get_rect(center=(x, y))
        self.dir = 0

    def update(self):
        x = WIDTH/2+self.rw*math.cos(self.dir*math.pi/180)
        y = HEIGHT/2+self.rh*math.sin(self.dir*math.pi/180)
        self.rect = self.image.get_rect(center=(x, y))
        self.dir += 1

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('楕円の円周上の座標')
clock = pg.time.Clock()

rw, rh = 100, 200 # 横半径、縦半径
all_ellipses = pg.sprite.Group()
all_ellipses.add(Planet(False))
all_ellipses.add(Satellite())
all_ellipses.add(Planet(True))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_ellipses.update()
    screen.fill(pg.Color('black'))
    all_ellipses.draw(screen)

    pg.display.update()
    clock.tick(FPS)

pg.quit()
