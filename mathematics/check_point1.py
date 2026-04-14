import pygame as pg, sys, math

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('円周上の座標')
font = pg.font.SysFont('sans-self', 30)
text = font.render('こんにちは', True, (0,0,0))

while True:
    screen.fill(pg.Color('white'))
    screen.blit(text,(200-text.get_width()/2,
                      200-text.get_height()/2))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()