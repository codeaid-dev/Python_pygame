import pygame as pg, sys, random

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

while True:
    screen.fill(pg.Color('white'))
    for t in tiles:
        t.draw()
    txt = font.render('Memory all',True,(255,0,0))
    screen.blit(txt,((WIDTH-txt.get_width())/2,50))

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()