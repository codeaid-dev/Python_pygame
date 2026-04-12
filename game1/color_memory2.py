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

colors = [(255,0,0),
          (0,255,0),
          (0,0,255),
          (255,255,0),
          (0,255,255),
          (255,0,255)]
random.shuffle(colors)
tiles = []
for i in range(6):
    tiles.append(Tile(50+i%3*200,
                      100+i//3*150,
                      colors[i]))
font = pg.font.SysFont('helvetica', 30)
saved_time = time.time()
status = 0 # 0:memory, 1:doing, 2:show

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
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()