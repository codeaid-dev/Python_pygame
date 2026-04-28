import pygame as pg, math

WIDTH, HEIGHT = 500, 500
FPS = 60
class Circle(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.mx, self.my = WIDTH/2,HEIGHT/2

    def update(self):
        self.mx,self.my = pg.mouse.get_pos()
        self.image.fill((0, 0, 0, 0))
        pg.draw.circle(self.image,(70,120,200),
                       (WIDTH/2,HEIGHT/2),250)
        self.follow_eye(150,250)
        self.follow_eye(350,250)

    def follow_eye(self,x,y):
        pg.draw.circle(self.image,(255,255,255),
                       (x,y),50)
        angle = math.atan2(self.my-y,self.mx-x)
        ex = x+math.cos(angle)*20
        ey = y+math.sin(angle)*20
        pg.draw.circle(self.image, (0,0,0),
                       (ex,ey), 25)

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('目がマウスに向く')
clock = pg.time.Clock()

all_circles = pg.sprite.Group()
all_circles.add(Circle())

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_circles.update()
    screen.fill(pg.Color('white'))
    all_circles.draw(screen)

    pg.display.update()
    clock.tick(FPS)

pg.quit()
