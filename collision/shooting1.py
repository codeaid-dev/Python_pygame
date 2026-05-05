import pygame as pg

WIDTH, HEIGHT = 500, 800
FPS = 60
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('images/jiki.png')
        self.width,self.height = self.image.get_size()
        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT-self.height))
        self.speed = 5
        self.oto = pg.mixer.Sound('sounds/shoot.mp3')

    def update(self):
        x,y,w,h = self.rect
        key = pg.key.get_pressed()
        if key[pg.K_RIGHT]:
            x += self.speed
        if key[pg.K_LEFT]:
            x -= self.speed
        if key[pg.K_UP]:
            y -= self.speed
        if key[pg.K_DOWN]:
            y += self.speed

        if x > WIDTH-w:
            x -= self.speed
        if x < 0:
            x += self.speed
        if y > HEIGHT-h:
            y -= self.speed
        if y < 0:
            y += self.speed
        self.rect.topleft = (x,y)

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((10,10), pg.SRCALPHA)
        pg.draw.circle(self.image, (238,120,0), (5,5), 5)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        # 画面外に出たら削除
        if self.rect.bottom < 0:
            self.kill()

pg.init()
width,height = 500,800
screen = pg.display.set_mode((width,height))
pg.display.set_caption('シューティング')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.oto.play()
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)

    all_sprites.update()
    screen.fill(pg.Color('white'))
    all_sprites.draw(screen)
    pg.display.update()
    clock.tick(FPS)

pg.quit()
