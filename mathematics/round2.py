import pygame as pg, math

WIDTH, HEIGHT = 500, 500
FPS = 60
class Sun(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((20,20), pg.SRCALPHA)
        pg.draw.circle(self.image, (255,200,0), (10, 10), 10)
        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT/2))

class Planet(pg.sprite.Sprite):
    def __init__(self,direction):
        super().__init__()
        self.image = pg.Surface((6,6), pg.SRCALPHA)
        pg.draw.circle(self.image, (0,200,200), (3,3), 3)
        self.direction = direction
        self.position = 0
        self.update()

    def update(self):
        angle = self.direction * math.pi/180
        x = WIDTH/2 + self.position * math.cos(angle)
        y = HEIGHT/2 + self.position * math.sin(angle)
        self.rect = self.image.get_rect(center=(x, y))
        self.position += 2
        if self.position > 200:
            self.position = 0

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('図形の円周動作')
clock = pg.time.Clock()

all_circles = pg.sprite.Group()
all_circles.add(Sun())
for i in range(0,360,10):
    all_circles.add(Planet(i))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_circles.update()
    screen.fill(pg.Color('black'))
    # fade = pg.Surface((WIDTH,HEIGHT), pg.SRCALPHA)
    # fade.fill((0,0,0,30))
    # screen.blit(fade, (0,0))
    all_circles.draw(screen)

    pg.display.update()
    clock.tick(FPS)

pg.quit()

