import pygame as pg, sys

WINDOW_SIZE = WIDTH,HEIGHT = 600,600
pg.init()
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption('モンスター襲来')
player = pg.image.load('images/player.png')
playerW,playerH = player.get_size()
player = pg.transform.scale(player,(playerW/2,playerH/2))
playerW,playerH = player.get_size()
centerX = WIDTH/2
centerY = HEIGHT/2
angle = 0

while True:
    screen.fill(pg.Color('white'))
    newp = pg.transform.rotozoom(player, angle, 1)
    rect = newp.get_rect()
    rect.center = (centerX,centerY)
    screen.blit(newp, rect)
    key = pg.key.get_pressed()
    if key[pg.K_RIGHT]:
        angle -= 0.1
        if angle < -359:
            angle = 0
    if key[pg.K_LEFT]:
        angle += 0.1
        if angle > 359:
            angle = 0
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
