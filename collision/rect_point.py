import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((400,400))
pg.display.set_caption('マウスと矩形(四角形)の当たり判定')

def collision(mx,my,rx,ry,rw,rh):
    return rx < mx < rx+rw and ry < my < ry+rh

while True:
    screen.fill(pg.Color('white'))
    mx,my = pg.mouse.get_pos()
    rx = screen.get_width()/2-50
    ry = screen.get_height()/2-50
    target = pg.Rect(rx,ry,100,100)
    #if collision(mx,my,rx,ry,100,100):
    if target.collidepoint(mx,my):
        color = pg.Color(255,0,0)
    else:
        color = pg.Color(0,0,0)
    pg.draw.rect(screen,color,target)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
