import pygame as pg, math

WIDTH, HEIGHT = 300, 300
FPS = 60
class Circle(pg.sprite.Sprite):
    def __init__(self,position,direction):
        super().__init__()
        self.image = pg.Surface((10,10), pg.SRCALPHA)
        x = WIDTH/2 + position * math.cos(direction)
        y = HEIGHT/2 + position * math.sin(direction)
        pg.draw.circle(self.image, (0,0,0), (5, 5), 5)
        self.rect = self.image.get_rect(center=(x, y))

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('正多角形を描画')
clock = pg.time.Clock()

all_circles = pg.sprite.Group()
for i in range(5):
    all_circles.add(Circle(100, i*2*math.pi/5))

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

