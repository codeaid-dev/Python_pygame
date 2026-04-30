import pygame as pg, random

WIDTH, HEIGHT = 500, 500
FPS = 60
class Circle(pg.sprite.Sprite):
    def __init__(self, x, y, color, radius):
        super().__init__()
        self.speed = [random.randint(-5, 5), random.randint(-5, 5)]
        self.image = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.color = color
        self.radius = radius
        self.stop = False
        self.draw()

    def draw(self):
        self.image.fill((0, 0, 0, 0))
        pg.draw.circle(self.image, self.color,
                       (self.radius, self.radius),
                       self.radius)

    def update(self):
        if not self.stop:
            self.rect.move_ip(self.speed)
            self.x, self.y = self.rect.center
            if self.rect.left < 0 or self.rect.right > WIDTH:
                self.speed[0] *= -1
                self.color = random.choice([(255,0,0),(0,255,0),(0,0,255)])
            if self.rect.top < 0 or self.rect.bottom > HEIGHT:
                self.speed[1] *= -1
                self.color = random.choice([(255,0,0),(0,255,0),(0,0,255)])
        self.draw()

    def collision(self, x, y):
        dx = self.rect.centerx - x
        dy = self.rect.centery - y
        distance = (dx**2 + dy**2)**0.5
        return distance <= (self.radius)

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('円と円(点)の当たり判定')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
for i in range(6):
    x = random.randint(25,WIDTH-25)
    y = random.randint(25,HEIGHT-25)
    color = random.choice([(255,0,0),(0,255,0),(0,0,255)])
    enemy = Circle(x,y,color,25)
    all_sprites.add(enemy)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            push = True
        else:
            push = False

    all_sprites.update()
    if push:
        for sprite in all_sprites:
            mx,my = pg.mouse.get_pos()
            if sprite.collision(mx,my):
                sprite.stop = True
            sprite.draw()

    screen.fill(pg.Color('white'))
    all_sprites.draw(screen)
    pg.display.update()
    clock.tick(FPS)

pg.quit()
