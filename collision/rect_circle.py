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

    def update(self,player=None):
        if player and self.collision(player):
            self.color = (255,0,0,150)
        else:
            self.color = (255,0,0)
        self.draw()

    def collision(self,player):
        cx,cy = player.rect.center
        if cx < self.x:
            closestX = self.x
        elif cx > self.x + self.rw:
            closestX = self.x + self.rw
        else:
            closestX = cx
        
        if cy < self.y:
            closestY =self.y
        elif cy > self.y + self.rh:
            closestY = self.y + self.rh
        else:
            closestY = cy
        
        dx = cx - closestX
        dy = cy - closestY
        distance = (dx**2 + dy**2)**0.5
        return distance < player.radius

class Circle(pg.sprite.Sprite):
    def __init__(self, x, y, color, radius):
        super().__init__()
        self.image = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.color = color
        self.radius = radius
        self.draw()

    def draw(self):
        self.image.fill((0, 0, 0, 0))
        pg.draw.circle(self.image, self.color,
                       (self.radius, self.radius),
                       self.radius)

    def update(self,player):
        mx,my = pg.mouse.get_pos()
        self.rect.center = (mx, my)

pg.init()
screen = pg.display.set_mode((400,400))
pg.display.set_caption('円と矩形(四角形)の当たり判定')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Circle(30,30,(100,150,250),30)
target = Rect(WIDTH/2-50,HEIGHT/2-50,(255,0,0),100,100)
all_sprites.add(player, target)

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
