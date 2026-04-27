import pygame as pg, math

WIDTH, HEIGHT = 600, 500
FPS = 60
class Wave(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(0, 0))

    def update(self):
        mx,my = pg.mouse.get_pos()
        self.image.fill((0, 0, 0, 0))
        for x in range(600):
            y = HEIGHT/2+math.sin((x+mx)*0.01)*my
            pg.draw.circle(self.image, (0, 0, 0),
                        (x, y), 1)

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('波を描く')
clock = pg.time.Clock()

all_circles = pg.sprite.Group()
all_circles.add(Wave())

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
