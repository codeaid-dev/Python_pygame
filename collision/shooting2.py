import pygame as pg, random

WIDTH, HEIGHT = 500, 800
FPS = 60
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('images/jiki.png')
        self.explosion_image = pg.image.load('images/bakuhatsu.png')
        self.width,self.height = self.image.get_size()
        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT-self.height))
        self.speed = 5
        self.oto = pg.mixer.Sound('sounds/shoot.mp3')
        self.explosion_oto = pg.mixer.Sound('sounds/explosion.mp3')
        self.alive = True

    def update(self):
        if not self.alive:
            return

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

    def explode(self):
        self.explosion_oto.play()
        self.image = self.explosion_image
        self.alive = False

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

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('images/teki.png')
        self.width,self.height = self.image.get_size()
        x = random.randint(self.width//2,WIDTH-self.width//2)
        y = random.randint(-HEIGHT-self.height//2,-self.height//2)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
        self.active = True

    def update(self):
        if not self.active:
            return

        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            x = random.randint(self.width//2,WIDTH-self.width//2)
            y = random.randint(-HEIGHT-self.height//2,-self.height//2)
            self.rect.center = (x,y)

pg.init()
width,height = 500,800
screen = pg.display.set_mode((width,height))
pg.display.set_caption('シューティング')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
bullets = pg.sprite.Group()
enemies = pg.sprite.Group()
player = Player()
all_sprites.add(player)
for _ in range(20):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and player.alive:
                player.oto.play()
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

    all_sprites.update()
    pg.sprite.groupcollide(bullets,enemies,True,True)
    hits = pg.sprite.spritecollide(player,enemies,True)
    if hits:
        player.explode()
        for enemy in enemies:
            enemy.active = False
    screen.fill(pg.Color('white'))
    all_sprites.draw(screen)
    pg.display.update()
    clock.tick(FPS)

pg.quit()
