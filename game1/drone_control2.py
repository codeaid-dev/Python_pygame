import pygame as pg, random

WIDTH, HEIGHT = 500, 500
FPS = 60
class Drone(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        img = pg.image.load('images/drone_red.png')
        width,height = img.get_size()
        self.image = pg.transform.scale(img, (width/3,height/3))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        x,y,w,h = self.rect
        key = pg.key.get_pressed()
        if key[pg.K_UP]:
            y -= self.speed
        if key[pg.K_DOWN]:
            y += self.speed
        if key[pg.K_RIGHT]:
            x += self.speed
        if key[pg.K_LEFT]:
            x -= self.speed

        if x < -w:
            x = WIDTH
        if x > WIDTH:
            x = -w
        if y < -h:
            y = HEIGHT
        if y > HEIGHT:
            y = -h
        self.rect.topleft = (x,y)

class Bit(pg.sprite.Sprite):
    def __init__(self, x, y, color, rw, rh):
        super().__init__()
        self.image = pg.Surface((rw, rh), pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.color = color
        self.dx = random.randint(-4,4)
        self.dy = random.randint(-4,4)
        self.alive = True
        self.draw()

    def draw(self):
        self.image.fill((0, 0, 0, 0))
        pg.draw.rect(self.image, self.color,
                     pg.Rect(0,0,self.rect.w,self.rect.h))

    def update(self):
        if not self.alive:
            self.kill()
            return
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.dx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy *= -1

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('ドローンを操作する')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
drone = Drone(WIDTH/2,HEIGHT/2)
all_sprites.add(drone)
bits = pg.sprite.Group()
for _ in range(100):
    bit = Bit(random.randint(0,490),
              random.randint(0,490),
              (255,0,0),10,10)
    bits.add(bit)
    all_sprites.add(bit)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_sprites.update()
    for bit in bits.sprites():
        if bit.rect.colliderect(drone):
            bit.alive = False
    screen.fill(pg.Color('white'))
    all_sprites.draw(screen)
    pg.display.update()
    clock.tick(FPS)

pg.quit()
