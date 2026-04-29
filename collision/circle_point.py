import pygame as pg

WIDTH, HEIGHT = 400, 400
FPS = 60
class Circle(pg.sprite.Sprite):
    def __init__(self, x, y, color, radius):
        super().__init__()
        self.image = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.color = color
        self.radius = radius
        self.mx, self.my = 0,0
        self.draw()

    def draw(self):
        self.image.fill((0, 0, 0, 0))
        pg.draw.circle(self.image, self.color,
                       (self.radius, self.radius),
                       self.radius)

    def update(self):
        self.mx,self.my = pg.mouse.get_pos()

    def collision(self):
        dx = self.rect.centerx - self.mx
        dy = self.rect.centery - self.my
        distance = (dx**2 + dy**2)**0.5
        return distance <= (self.radius)

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('円と円(点)の当たり判定')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
enemy = Circle(WIDTH/2,HEIGHT/2,(255,0,0),50)
all_sprites.add(enemy)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_sprites.update()
    for sprite in all_sprites:
        if sprite.collision():
            sprite.color = (0,0,255)
        else:
            sprite.color = (255,0,0)
        sprite.draw()

    screen.fill(pg.Color('white'))
    all_sprites.draw(screen)
    pg.display.update()
    clock.tick(FPS)

pg.quit()
