import pygame as pg, sys, math

WINDOW_SIZE = WIDTH,HEIGHT = 600,600
FPS = 60
pg.init()
screen = pg.display.set_mode(WINDOW_SIZE)
clock = pg.time.Clock()
pg.display.set_caption('モンスター襲来')
player = pg.image.load('images/player.png')
playerW,playerH = player.get_size()
player = pg.transform.scale(player,(playerW/2,playerH/2))
playerW,playerH = player.get_size()
centerX = WIDTH/2
centerY = HEIGHT/2
angle = 0
bullets = []
otoB = pg.mixer.Sound('sounds/gun.mp3')

class Sprite:
    pass

while True:
    screen.fill(pg.Color('white'))
    newp = pg.transform.rotozoom(player, angle, 1)
    rect = newp.get_rect()
    rect.center = (centerX,centerY)
    screen.blit(newp, rect)
    key = pg.key.get_pressed()
    if key[pg.K_RIGHT]:
        angle -= 1
        if angle < -359:
            angle = 0
    if key[pg.K_LEFT]:
        angle += 1
        if angle > 359:
            angle = 0

    for b in bullets:
        pg.draw.circle(screen, pg.Color(255,0,0), (b.x,b.y), 5)
        b.x += 3*math.cos(math.radians(b.angle))
        b.y += 3*math.sin(math.radians(b.angle))
        if 0 > b.x or b.x > WIDTH or 0 > b.y or b.y > HEIGHT:
            bullets.remove(b)

    pg.display.update()
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                otoB.play()
                b = Sprite()
                b.angle = (angle*-1)-90
                b.x = centerX+playerH/2*math.cos(math.radians(b.angle))
                b.y = centerY+playerH/2*math.sin(math.radians(b.angle))
                bullets.append(b)
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
