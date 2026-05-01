import pygame as pg

WIDTH, HEIGHT = 400, 400
FPS = 60
class Rect(pg.sprite.Sprite):
    def __init__(self, x, y, color, rw, rh, is_player=False):
        super().__init__()
        self.image = pg.Surface((rw, rh), pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x,self.y = x,y
        self.rw,self.rh = rw,rh
        self.color = color
        self.is_player = is_player
        self.draw()

    def draw(self):
        self.image.fill((0, 0, 0, 0))
        pg.draw.rect(self.image, self.color,
                     pg.Rect(0,0,self.rw,self.rh))

    def update(self):
        if self.is_player:
            mx,my = pg.mouse.get_pos()
            self.rect.center = (mx, my)

    def collision(self,other):
        return other.rect.left <= self.rect.right \
            and self.rect.left <= other.rect.right \
            and other.rect.top <= self.rect.bottom \
            and self.rect.top <= other.rect.bottom

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('矩形(四角形)と矩形(四角形)の当たり判定')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Rect(30,30,(100,150,250),100,100,True)
enemy = Rect(WIDTH/2-50,HEIGHT/2-50,(255,0,0),100,100,False)
all_sprites.add(player, enemy)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_sprites.update()
    for sprite in all_sprites:
        if sprite is player:
            continue
        if sprite.collision(player):
        # if sprite.rect.colliderect(player):
            sprite.color = (255,0,0,150)
        else:
            sprite.color = (255,0,0)
        sprite.draw()

    screen.fill(pg.Color('white'))
    all_sprites.draw(screen)
    pg.display.update()
    clock.tick(FPS)

pg.quit()
