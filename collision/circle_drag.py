import pygame as pg, random

WIDTH, HEIGHT = 500, 500
FPS = 60
class Circle(pg.sprite.Sprite):
    def __init__(self, x, y, color, radius):
        super().__init__()
        self.image = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.x,self.y = x,y
        self.color = color
        self.radius = radius
        self.draw()

    def draw(self):
        self.image.fill((0, 0, 0, 0))
        pg.draw.circle(self.image, self.color,
                       (self.radius, self.radius),
                       self.radius)

    def is_hit(self, pos):
        mx,my = pos
        return (mx-self.x)**2 + (my-self.y)**2 <= self.radius**2

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('円を掴んで動かす')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
for _ in range(5):
    x = random.randint(25,WIDTH-25)
    y = random.randint(25,HEIGHT-25)
    color = (random.randint(0,255),
             random.randint(0,255),
             random.randint(0,255))
    enemy = Circle(x,y,color,25)
    all_sprites.add(enemy)

dragging = None
offset_x = 0
offset_y = 0
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            for c in reversed(all_sprites.sprites()):
                if c.is_hit(event.pos):
                    dragging = c
                    offset_x = c.x - event.pos[0]
                    offset_y = c.y - event.pos[1]
                    # 前面へ
                    all_sprites.remove(c)
                    all_sprites.add(c)
                    break
        elif event.type == pg.MOUSEBUTTONUP:
            dragging = None
        elif event.type == pg.MOUSEMOTION:
            if dragging:
                dragging.x = event.pos[0]+offset_x
                dragging.y = event.pos[1]+offset_y
                dragging.rect.center = (dragging.x,dragging.y)

    all_sprites.update()
    screen.fill(pg.Color('white'))
    all_sprites.draw(screen)
    pg.display.update()
    clock.tick(FPS)

pg.quit()
