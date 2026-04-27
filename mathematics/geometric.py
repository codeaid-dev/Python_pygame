import pygame as pg, math

WIDTH, HEIGHT = 500, 500
FPS = 60
class Circle(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.radius = 125
        self.dir = 0

    def update(self):
        x = WIDTH/2+self.radius*math.cos(math.radians(self.dir))
        y = HEIGHT/2+self.radius*math.sin(math.radians(self.dir))
        pg.draw.circle(self.image,(255,255,255),(x,y),2)
        mx = x+self.radius*math.cos(math.radians(self.dir)*36)
        my = y+self.radius*math.sin(math.radians(self.dir)*36)
        pg.draw.circle(self.image,(255,0,0),(mx,my),2)
        self.dir += 0.1

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('幾何学模様')
clock = pg.time.Clock()

all_circles = pg.sprite.Group()
all_circles.add(Circle())

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_circles.update()
    screen.fill(pg.Color('black'))
    all_circles.draw(screen)

    pg.display.update()
    clock.tick(FPS)

pg.quit()
