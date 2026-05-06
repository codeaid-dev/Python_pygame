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

class Ufo(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img = pg.image.load('images/ufo.png')
        width,height = img.get_size()
        self.image = pg.transform.scale(img, (width/8,height/8))
        width,height = self.image.get_size()
        x = random.randint(0,WIDTH-width)
        y = random.randint(0,HEIGHT-height)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = [random.randint(-4, 4), random.randint(-4, 4)]
        self.alive = True

    def update(self):
        if not self.alive:
            self.kill()
            return
        self.rect.move_ip(self.speed)
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed[1] *= -1

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
ufos = pg.sprite.Group()
for _ in range(5):
    ufo = Ufo()
    ufos.add(ufo)
    all_sprites.add(ufo)

clear,over = False,False
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_sprites.update()
    for bit in bits.sprites():
        if bit.rect.colliderect(drone):
            bit.alive = False

    for ufo in ufos.sprites():
        if ufo.rect.colliderect(drone):
            ufo.alive = False

    screen.fill(pg.Color('white'))
    all_sprites.draw(screen)
    if len(ufos.sprites())==0 and not clear:
        over = True

    if len(bits.sprites())==0 and not over:
        clear = True

    if over:
        font = pg.font.SysFont('Helvetica',30)
        text = font.render('GAME OVER',
                           True,(0,0,0))
        screen.blit(text,
                   ((WIDTH-text.get_width())/2,
                   (HEIGHT-text.get_height())/2))

    if clear:
        font = pg.font.SysFont('Helvetica',30)
        text = font.render('GAME CLEAR',
                           True,(0,0,0))
        screen.blit(text,
                   ((WIDTH-text.get_width())/2,
                   (HEIGHT-text.get_height())/2))

    pg.display.update()
    clock.tick(FPS)

pg.quit()
