import pygame as pg, math

WIDTH, HEIGHT = 500, 500
FPS = 60
class Circle(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.dir = 0

    def update(self):
        self.image.fill((0, 0, 0, 0))
        x = WIDTH/2+0*math.cos(self.dir*math.pi/180)
        y = HEIGHT/2+200*math.sin(self.dir*math.pi/180)

        pg.draw.circle(self.image, (0, 0, 0),
                       (x, y), 10)
        self.dir += 1

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('円周上の座標')
clock = pg.time.Clock()

all_circles = pg.sprite.Group()
all_circles.add(Circle())

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
