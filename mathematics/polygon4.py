import pygame as pg, math

WIDTH, HEIGHT = 500, 500
FPS = 60
class Polygon(pg.sprite.Sprite):
    def __init__(self,x,y,radius,num):
        super().__init__()
        self.image = pg.Surface((radius*2,radius*2), pg.SRCALPHA)
        vertices = []
        for i in range(num):
            px = radius + radius * math.cos(i*math.radians(360/num))
            py = radius + radius * math.sin(i*math.radians(360/num))
            vertices.append([px,py])
        pg.draw.polygon(self.image, (0,0,0), vertices)
        self.rect = self.image.get_rect(center=(x, y))

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('正多角形を描画')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
p=5
for y in range(3):
    for x in range(3):
        px = 100+x*150
        py = 100+y*150
        all_sprites.add(Polygon(px,py,50,p))
        p += 1

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_sprites.update()
    screen.fill(pg.Color('white'))
    all_sprites.draw(screen)

    pg.display.update()
    clock.tick(FPS)

pg.quit()

