import pygame as pg, sys, random, time

WINDOW_SIZE = WIDTH,HEIGHT = 500,500
pg.init()
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption('円を運ぶ')

finish = False
over = False
circles = []
class Circle:
    pass
for i in range(20):
    c = Circle()
    c.x = random.randint(25,WIDTH-25)
    c.y = random.randint(int(HEIGHT/2)+25,HEIGHT-25)
    c.radius = 25
    c.status = False
    circles.append(c)
drag = False
start = time.time()
font = pg.font.SysFont('helvetica', 30)

while True:
    screen.fill(pg.Color('white'))
    pg.draw.line(screen,
                pg.Color('black'),
                (0,HEIGHT/2),
                (WIDTH,HEIGHT/2), 5)
    count = 0
    for c in circles:
        pg.draw.circle(screen,
                       pg.Color('black'),
                       (c.x,c.y), c.radius)
        if c.y < HEIGHT/2:
            count += 1
    if count >= 20:
        finish = True
    timer = int(time.time()-start)
    if (timer >= 20 and finish == False) or over:
        txt = font.render('Time is up..',True,(255,0,0))
        screen.blit(txt,((WIDTH-txt.get_width())/2,
                        (HEIGHT-txt.get_height())/2+30))
        over = True
    elif finish:
        txt = font.render('Finish',True,(255,0,0))
        screen.blit(txt,((WIDTH-txt.get_width())/2,
                        (HEIGHT-txt.get_height())/2+30))
    else:
        txt = font.render(f'{20-timer:.0f}',True,(255,0,0))
        screen.blit(txt,((WIDTH-txt.get_width())/2,
                        (HEIGHT-txt.get_height())/2+30))

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            x,y = pg.mouse.get_pos()
            for c in circles:
                distance = ((x-c.x)**2 + (y-c.y)**2)**0.5
                if distance < c.radius:
                    c.ox = x
                    c.oy = y
                    c.status = True
                else:
                    c.status = False
            drag = True
        if event.type == pg.MOUSEBUTTONUP:
            drag = False
        if event.type == pg.MOUSEMOTION and drag:
            x,y = pg.mouse.get_pos()
            for c in circles:
                if c.status:
                    mx = x-c.ox
                    my = y-c.oy
                    c.x += mx
                    c.y += my
                    c.ox = x
                    c.oy = y
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()