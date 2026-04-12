import pygame as pg, sys, math

WIDTH,HEIGHT = 800,600
pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('ミサイルコマンド')
clock = pg.time.Clock()
angle = 0
missiles = []

class Missile:
    pass

def target():
    mx,my = pg.mouse.get_pos()
    pg.draw.line(screen, (0,0,255), (mx-10,my), (mx+10,my), 5)
    pg.draw.line(screen, (0,0,255), (mx,my-10), (mx,my+10), 5)

def move_missile():
    for m in missiles:
        pg.draw.line(screen, (0,0,255), (WIDTH/2,HEIGHT-50), (m.x,m.y), 2)
        pg.draw.circle(screen, (255,255,255), (m.x,m.y), m.radius)
        if not ((m.goalX-1<=int(m.x)<=m.goalX+1) and \
                (m.goalY-1<=int(m.y)<=m.goalY+1)):
            m.x += math.cos(m.angle)*2
            m.y += math.sin(m.angle)*2

def create_missile():
    m = Missile()
    m.goalX,m.goalY = pg.mouse.get_pos()
    m.x = WIDTH/2
    m.y = HEIGHT-50
    x = m.goalX-m.x
    y = m.goalY-m.y
    m.angle = math.atan2(y,x)
    m.radius = 5
    missiles.append(m)

while True:
    screen.fill(pg.Color('black'))
    target()
    move_missile()
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            create_missile()
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    clock.tick(60)