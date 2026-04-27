import pygame as pg, math, random

WIDTH, HEIGHT = 500, 500
FPS = 60
class Circle(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((30, 30), pg.SRCALPHA)
        pg.draw.circle(self.image,(0,0,0),(15,15),15)
        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT/2))
        self.x, self.y = WIDTH/2, HEIGHT/2
        self.speed = 5
        self.dir = random.randint(0,360)

    def update(self):
        self.x += self.speed*math.cos(math.radians(self.dir))
        self.y += self.speed*math.sin(math.radians(self.dir))
        if self.x < 15 or self.x > WIDTH-15:
            self.dir = 180-self.dir
        if self.y < 15 or self.y > HEIGHT-15:
            self.dir *= -1
        self.rect = self.image.get_rect(center=(self.x, self.y))

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('円が画面内をウロウロする')
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
