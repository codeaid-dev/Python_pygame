import pygame as pg

WIDTH, HEIGHT = 500, 500
FPS = 60
class Circle(pg.sprite.Sprite):
    def __init__(self,radius):
        super().__init__()
        self.image = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
        pg.draw.circle(self.image, (0,0,0), (radius, radius), radius)
        self.x, self.y = WIDTH/2, HEIGHT/2
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.radius = radius

    def update(self):
        self.x,self.y = pg.mouse.get_pos()
        self.rect.center = (self.x, self.y)

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('円をマウスで動かす')
clock = pg.time.Clock()

all_circles = pg.sprite.Group()
all_circles.add(Circle(25))

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
