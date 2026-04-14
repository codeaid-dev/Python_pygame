import pygame as pg, sys

WIDTH, HEIGHT = 500, 500
FPS = 60
pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('画像表示')
clock = pg.time.Clock()
img = pg.image.load('images/panda.png')

while True:
    screen.fill(pg.Color('white'))
    screen.blit(img, (0,79))
    pg.display.update()
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()