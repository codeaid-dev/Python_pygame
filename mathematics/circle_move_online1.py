import pygame as pg, math

WIDTH, HEIGHT = 500, 500
FPS = 60
class Circle(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.lx1, self.ly1 = 100,100
        self.lx2, self.ly2 = 400,400
        self.cx, self.cy = self.lx1, self.ly1

    def update(self):
        self.image.fill((0, 0, 0, 0))
        dx = self.lx2 - self.cx
        dy = self.ly2 - self.cy
        angle = math.atan2(dx,dy)
        self.cx += math.cos(angle)*2
        self.cy += math.sin(angle)*2

        pg.draw.line(self.image, (0,0,0),
                     (self.lx1,self.ly1),
                     (self.lx2,self.ly2), 1)
        pg.draw.circle(self.image, (0, 0, 0),
                       (self.cx, self.cy), 30)

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('線上で円が移動する')
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
