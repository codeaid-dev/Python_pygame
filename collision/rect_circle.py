import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((400,400))
pg.display.set_caption('円と矩形(四角形)の当たり判定')

def collision(cx,cy,cr,t):
    if cx < t.x:
        closestX = t.x
    elif cx > t.x + t.w:
        closestX = t.x + t.w
    else:
        closestX = cx
    
    if cy < t.y:
        closestY =t.y
    elif cy > t.y + t.h:
        closestY = t.y + t.h
    else:
        closestY = cy
    
    dx = cx - closestX
    dy = cy - closestY
    distance = (dx**2 + dy**2)**0.5
    return distance < cr

while True:
    screen.fill(pg.Color('white'))
    mx,my = pg.mouse.get_pos()
    mr = 30
    rx = screen.get_width()/2-50
    ry = screen.get_height()/2-50
    target = pg.Rect(rx,ry,100,100)
    if collision(mx,my,mr,target):
        color = pg.Color(255,0,0)
    else:
        color = pg.Color(0,0,0)
    pg.draw.rect(screen,color,target)
    pg.draw.circle(screen,pg.Color(100,150,250),
                   (mx,my),mr)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
