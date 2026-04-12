import pygame as pg, sys, random, time

WINDOW_SIZE = WIDTH,HEIGHT = 600,400
pg.init()
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption('色記憶')

class Tile:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c
    def draw(self,c=None):
        if c==None:
            color = self.c
        else:
            color = c
        rect = pg.Rect(self.x,self.y,100,100)
        pg.draw.rect(screen,color,rect)

class Circle:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c
        self.radius = 25
    def draw(self):
        pg.draw.circle(screen,self.c,
                       (self.x,self.y),
                       self.radius)

colors = [(255,0,0),
          (0,255,0),
          (0,0,255),
          (255,255,0),
          (0,255,255),
          (255,0,255)]
random.shuffle(colors)
tiles = []
circles = []
for i in range(6):
    tiles.append(Tile(50+i%3*200,
                      100+i//3*150,
                      colors[i]))
    circles.append(Circle(random.randint(25,WIDTH-24),
                          random.randint(25,75),
                          colors[i]))
font = pg.font.SysFont('helvetica', 30)
saved_time = time.time()
status = 0 # 0:memory, 1:doing, 2:show
drag = False

while True:
    screen.fill(pg.Color('white'))
    if status == 0:
        timer = 5 - int(time.time()-saved_time)
    elif status == 1:
        timer = 10 - int(time.time()-saved_time)
    else:
        timer = 0
    if timer == 0 and status != 2:
        status += 1
        if status == 1:
            saved_time = time.time()

    for t in tiles:
        if status == 0 or status == 2:
            t.draw()
        else:
            t.draw((200,200,200))

    for c in circles:
        c.draw()

    if status == 0:
        txt = font.render('Memory all',True,(255,0,0))
        screen.blit(txt,((WIDTH-txt.get_width())/2,50))
    elif status == 1:
        txt = font.render('Put all circles on each tile',True,(255,0,0))
        screen.blit(txt,((WIDTH-txt.get_width())/2,50))
    else:
        txt = font.render('Done',True,(255,0,0))
        screen.blit(txt,((WIDTH-txt.get_width())/2,50))
    txt = font.render(f'{timer}',True,(255,0,0))
    screen.blit(txt,((WIDTH-txt.get_width())/2,20))

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
        if event.type == pg.MOUSEMOTION and drag and status == 1:
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