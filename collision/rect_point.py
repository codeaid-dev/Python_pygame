import pygame as pg

WIDTH, HEIGHT = 400, 400
FPS = 60
class Rect(pg.sprite.Sprite):
    def __init__(self, x, y, color, rw, rh):
        super().__init__()
        self.image = pg.Surface((rw, rh), pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x,self.y = x,y
        self.rw,self.rh = rw,rh
        self.color = color
        self.draw()

    def draw(self):
        self.image.fill((0, 0, 0, 0))
        pg.draw.rect(self.image, self.color,
                     pg.Rect(0,0,self.rw,self.rh))

    def update(self):
        mx,my = pg.mouse.get_pos()
        # if self.rect.collidepoint(mx,my):
        if self.collision(mx,my):
            self.color = (255,0,0)
        else:
            self.color = (0,0,0)
        self.draw()

    def collision(self,mx,my):
        return self.x <= mx <= self.x+self.rw \
            and self.y <= my <= self.y+self.rh

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('マウスと矩形(四角形)の当たり判定')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
target = Rect(WIDTH/2-50,HEIGHT/2-50,(0,0,0),100,100)
all_sprites.add(target)

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
