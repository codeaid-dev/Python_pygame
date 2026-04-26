import pygame as pg, math

WIDTH, HEIGHT = 500, 500
FPS = 60
class Sun(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((40,40), pg.SRCALPHA)
        pg.draw.circle(self.image, (255,200,0), (20, 20), 20)
        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT/2))

class Earth(pg.sprite.Sprite):
    def __init__(self,position,direction):
        super().__init__()
        self.image = pg.Surface((80,80), pg.SRCALPHA)
        self.direction = direction
        self.position = position
        self.update()

    def update(self):
        self.image.fill((0,0,0,0))

        pg.draw.circle(self.image, (0,200,200), (40, 40), 10)

        mx = 40+30*math.cos(self.direction*12*math.pi/180)
        my = 40+30*math.sin(self.direction*12*math.pi/180)
        pg.draw.circle(self.image, (255,255,255), (mx,my), 2.5)

        angle = self.direction * math.pi/180
        x = WIDTH/2 + self.position * math.cos(angle)
        y = HEIGHT/2 + self.position * math.sin(angle)
        self.rect = self.image.get_rect(center=(x, y))

        self.direction += 0.5

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('地球')
clock = pg.time.Clock()

all_circles = pg.sprite.Group()
all_circles.add(Sun())
all_circles.add(Earth(200,0))

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
