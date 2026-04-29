import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((400,400))
pg.display.set_caption('円と円(点)の当たり判定')

def collision(x1,y1,r1,x2,y2,r2):
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return distance < r1+r2

while True:
    screen.fill(pg.Color('white'))
    mx,my = pg.mouse.get_pos()
    mr = 30
    cx = screen.get_width()/2
    cy = screen.get_height()/2
    cr = 50
    if collision(mx,my,mr,cx,cy,cr):
        color = pg.Color(255,0,0)
    else:
        color = pg.Color(0,0,0)
    pg.draw.circle(screen,color,(cx,cy),cr)
    pg.draw.circle(screen,pg.Color(100,150,250),(mx,my),mr)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
