import pygame as pg

WIDTH, HEIGHT = 400, 400
FPS = 60
class Ellipse(pg.sprite.Sprite):
    def __init__(self, x, y, color, w, h):
        super().__init__()
        self.image = pg.Surface((w, h), pg.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.color = color
        self.w, self.h = w,h
        self.mx, self.my = 0,0
        self.draw()

    def draw(self):
        self.image.fill((0, 0, 0, 0))
        pg.draw.ellipse(self.image, self.color,
                        (0,0,self.w,self.h))

    def update(self):
        self.mx,self.my = pg.mouse.get_pos()

    def collision(self):
        dx = self.rect.centerx - self.mx
        dy = self.rect.centery - self.my
        val = dx**2/(self.w/2)**2 + dy**2/(self.h/2)**2
        return val <= 1

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('点と楕円の当たり判定')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
target = Ellipse(WIDTH/2,HEIGHT/2,(255,0,0),100,200)
all_sprites.add(target)

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
