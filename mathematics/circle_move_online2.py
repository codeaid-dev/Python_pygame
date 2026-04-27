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
        self.target = (self.lx2,self.ly2)
        self.speed = 2

    def update(self):
        self.image.fill((0, 0, 0, 0))
        tx,ty = self.target
        dx = tx - self.cx
        dy = ty - self.cy
        dist = (dx**2 + dy**2)**0.5
        if dist < self.speed:
            self.cx, self.cy = tx, ty
            if self.target == (self.lx2, self.ly2):
                self.target = (self.lx1, self.ly1)
            else:
                self.target = (self.lx2, self.ly2)
        else:
            angle = math.atan2(dy,dx)
            self.cx += math.cos(angle)*self.speed
            self.cy += math.sin(angle)*self.speed
            # self.cx += dx / dist * self.speed
            # self.cy += dy / dist * self.speed

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
