import pygame as pg, random

WIDTH, HEIGHT = 400, 400
FPS = 60
class Rect(pg.sprite.Sprite):
    def __init__(self, x, y, color, rw, rh, is_player=False):
        super().__init__()
        self.speed = [random.randint(-5, 5), random.randint(-5, 5)]
        self.image = pg.Surface((rw, rh), pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.color = color
        self.rw,self.rh = rw,rh
        self.is_player = is_player
        self.stop = False
        self.draw()

    def draw(self):
        self.image.fill((0, 0, 0, 0))
        pg.draw.rect(self.image, self.color,
                     pg.Rect(0,0,self.rw,self.rh))

    def update(self,other):
        if self.is_player:
            mx,my = pg.mouse.get_pos()
            self.rect.center = (mx, my)
        elif other:
            if self.rect.colliderect(other.rect):
                self.stop = True
                self.color = (200,200,200)
                self.draw()
            else:
                if not self.stop:
                    self.rect.move_ip(self.speed)
                    if self.rect.left < 0 or self.rect.right > WIDTH:
                        self.speed[0] *= -1
                    if self.rect.top < 0 or self.rect.bottom > HEIGHT:
                        self.speed[1] *= -1

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('四角形が当たったら止まる(複数)')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Rect(30,30,(100,150,250),60,60,True)
all_sprites.add(player)
for _ in range(7):
    target = Rect(WIDTH/2,HEIGHT/2,(255,0,0),40,40)
    all_sprites.add(target)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_sprites.update(player)
    screen.fill(pg.Color('white'))
    all_sprites.draw(screen)
    pg.display.update()
    clock.tick(FPS)

pg.quit()
