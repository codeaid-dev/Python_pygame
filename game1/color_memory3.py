import pygame as pg, random, time

WIDTH,HEIGHT = 600,400
FPS = 60
pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('色記憶')
clock = pg.time.Clock()

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

class Circle(pg.sprite.Sprite):
    def __init__(self, x, y, color, radius):
        super().__init__()
        self.image = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.x,self.y = x,y
        self.color = color
        self.radius = radius
        self.draw()
    def draw(self):
        self.image.fill((0, 0, 0, 0))
        pg.draw.circle(self.image, self.color,
                       (self.radius, self.radius),
                       self.radius)
    def is_hit(self, pos):
        mx,my = pos
        return (mx-self.x)**2 + (my-self.y)**2 <= self.radius**2

colors = [(255,0,0),
          (0,255,0),
          (0,0,255),
          (255,255,0),
          (0,255,255),
          (255,0,255)]
random.shuffle(colors)
tiles = []
all_sprites = pg.sprite.Group()
for i in range(6):
    tiles.append(Tile(50+i%3*200,
                      100+i//3*150,
                      colors[i]))
    x = random.randint(25,WIDTH-25)
    y = random.randint(25,75)
    c = Circle(x,y,colors[i],25)
    all_sprites.add(c)
font = pg.font.SysFont('helvetica', 30)
saved_time = time.time()
status = 0 # 0:memory, 1:doing, 2:show
dragging = None
offset_x = 0
offset_y = 0
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            for c in reversed(all_sprites.sprites()):
                if c.is_hit(event.pos):
                    dragging = c
                    offset_x = c.x - event.pos[0]
                    offset_y = c.y - event.pos[1]
                    # 前面へ
                    all_sprites.remove(c)
                    all_sprites.add(c)
                    break
        elif event.type == pg.MOUSEBUTTONUP:
            dragging = None
        elif event.type == pg.MOUSEMOTION:
            if dragging:
                dragging.x = event.pos[0]+offset_x
                dragging.y = event.pos[1]+offset_y
                dragging.rect.center = (dragging.x,dragging.y)

    all_sprites.update()
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

    all_sprites.draw(screen)
    pg.display.update()
    clock.tick(FPS)
pg.quit()
