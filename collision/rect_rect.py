import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((400,400))
pg.display.set_caption('矩形(四角形)と矩形(四角形)の当たり判定')

def collision(target,you):
    return you.left <= target.right \
        and target.left <= you.right \
        and you.top <= target.bottom \
        and target.top <= you.bottom

while True:
    screen.fill(pg.Color('white'))
    mx,my = pg.mouse.get_pos()
    you = pg.Rect(mx,my,120,120)
    rx = screen.get_width()/2-50
    ry = screen.get_height()/2-50
    target = pg.Rect(rx,ry,100,100)
    if collision(target,you):
    #if target.colliderect(you):
        color = pg.Color(255,0,0)
    else:
        color = pg.Color(0,0,0)
    pg.draw.rect(screen,pg.Color(100,150,250),you)
    pg.draw.rect(screen,color,target)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
