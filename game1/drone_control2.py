import pygame as pg, sys, random

class Character:
    pass

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('ドローンを操作する')
drone = pg.image.load('images/drone_red.png')
width,height = drone.get_size()
drone = pg.transform.scale(drone,(width/3,height/3))
width,height = drone.get_size()
x,y = (500-width)/2,(500-height)/2
speed = 5
targets = []
for i in range(100):
    target = Character()
    target.rect = pg.Rect(random.randint(0,490),random.randint(0,490),10,10)
    target.flag = False
    target.dx = random.randint(1,4)
    target.dy = random.randint(1,4)
    targets.append(target)

while True:
    screen.fill(pg.Color('white'))
    key = pg.key.get_pressed()
    if key[pg.K_UP]:
        y -= speed
    if key[pg.K_DOWN]:
        y += speed
    if key[pg.K_RIGHT]:
        x += speed
    if key[pg.K_LEFT]:
        x -= speed

    if x < -width:
        x = 500
    if x > 500:
        x = -width
    if y < -height:
        y = 500
    if y > 500:
        y = -height

    pr = screen.blit(drone, (x,y))

    for t in targets:
        if t.rect.colliderect(pr):
            t.flag = True
            continue
        if not t.flag:
            t.rect.x += t.dx
            t.rect.y += t.dy
            if t.rect.x < 0 or t.rect.x > 490:
                t.dx *= -1
            if t.rect.y < 0 or t.rect.y > 490:
                t.dy *= -1
            pg.draw.rect(screen, pg.Color('red'), t.rect)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()