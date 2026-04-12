import pygame as pg, sys, math, random, time

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
enemies = []
start = time.time()
interval = 2
monster = pg.image.load('images/monster-77x50.png')
monsterW,monsterH = monster.get_size()
over = False
score = 0
bomb1 = pg.mixer.Sound('sounds/bomb1.mp3')
bomb2 = pg.mixer.Sound('sounds/bomb2.mp3')

class Sprite:
    pass

def collision(x1,y1,r1,x2,y2,r2):
    dst = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return dst < r1+r2

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
        for e in enemies:
            if collision(b.x,b.y,5,e.x,e.y,monsterH/2):
                enemies.remove(e)
                bomb1.play()
                score += 1

    if interval < int(time.time()-start) and not over:
        start = time.time()
        interval -= 0.1
        if interval <= 0:
            interval = 2
        e = Sprite()
        direction = random.randint(0,359)
        e.x = centerX+WIDTH*math.cos(math.radians(direction))
        e.y = centerY+HEIGHT*math.sin(math.radians(direction))
        x = centerX-e.x
        y = centerY-e.y
        e.angle = math.atan2(y,x)
        enemies.append(e)

    for e in enemies:
        screen.blit(monster, (e.x-monsterW/2,e.y-monsterH/2))
        #pg.draw.circle(screen, pg.Color(100,100,200), (e.x,e.y), 25)
        e.x += 1.2*math.cos(e.angle)
        e.y += 1.2*math.sin(e.angle)
        if collision(e.x,e.y,monsterH/2,centerX,centerY,rect.h/2):
            enemies.remove(e)
            bomb2.play()
            over = True

    if over:
        font = pg.font.SysFont('helvetica', 30)
        txt = font.render(f'GAME OVER SCORE: {score}',True,(0,0,0))
        screen.blit(txt,((WIDTH-txt.get_width())/2,(HEIGHT-txt.get_height())/2))

    pg.display.update()
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and not over:
                otoB.play()
                b = Sprite()
                b.angle = (angle*-1)-90
                b.x = centerX+playerH/2*math.cos(math.radians(b.angle))
                b.y = centerY+playerH/2*math.sin(math.radians(b.angle))
                bullets.append(b)
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
