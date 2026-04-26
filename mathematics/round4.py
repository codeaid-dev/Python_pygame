import pygame as pg, math

WIDTH, HEIGHT = 500, 500
FPS = 60
class Ellipse(pg.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pg.Surface((5, 5), pg.SRCALPHA)
        pg.draw.circle(self.image, (0,0,0), (2.5, 2.5), 2.5)
        self.rect = self.image.get_rect(center=(x, y))

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('楕円の円周上の座標')
clock = pg.time.Clock()

rw, rh = 100, 200 # 横半径、縦半径
all_ellipses = pg.sprite.Group()
for i in range(0,360,10):
    rad = i * math.pi/180
    x = WIDTH/2+rw*math.cos(rad)
    y = HEIGHT/2+rh*math.sin(rad)

    all_ellipses.add(Ellipse(x,y))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_ellipses.update()
    screen.fill(pg.Color('white'))
    all_ellipses.draw(screen)

    pg.display.update()
    clock.tick(FPS)

pg.quit()
