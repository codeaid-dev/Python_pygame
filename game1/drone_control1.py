import pygame as pg

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

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('ドローンを操作する')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
drone = Drone(WIDTH/2,HEIGHT/2)
all_sprites.add(drone)

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
