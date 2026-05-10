import pygame as pg, math

WIDTH, HEIGHT = 500, 500
FPS = 60
class Ellipse(pg.sprite.Sprite):
    def __init__(self, x, y, color, w, h, is_player=False):
        super().__init__()
        self.image = pg.Surface((w, h), pg.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.color = color
        self.w, self.h = w,h
        self.x, self.y = x,y
        self.is_player = is_player
        self.draw()

    def draw(self):
        self.image.fill((0, 0, 0, 0))
        pg.draw.ellipse(self.image, self.color,
                        (0,0,self.w,self.h))

    def update(self):
        if self.is_player:
            self.x,self.y = pg.mouse.get_pos()
            self.rect.center = (self.x, self.y)

    def collision(self,other):
        for i in range(0,360,5):
            t = i * (math.pi / 180)
            # otherの境界点
            ex = other.x + other.w/2 * math.cos(t)
            ey = other.y + other.h/2 * math.sin(t)
            # 中心までの距離
            dx = ex - self.x
            dy = ey - self.y
            # 自分の中に入っているかチェック
            if (dx**2)/((self.w/2)**2) + (dy**2)/((self.h/2)**2) <= 1:
                return True
        return False

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('点と楕円の当たり判定')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Ellipse(0,0,(0,255,0),200,100,True)
target = Ellipse(WIDTH/2,HEIGHT/2,(255,0,0),100,200)
all_sprites.add(player,target)

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
            sprite.color = (255,0,0,150)
        else:
            sprite.color = (255,0,0)
        sprite.draw()

    screen.fill(pg.Color('white'))
    all_sprites.draw(screen)
    pg.display.update()
    clock.tick(FPS)

pg.quit()
