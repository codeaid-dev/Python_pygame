import pygame as pg

WIDTH, HEIGHT = 500, 500
FPS = 60
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def normalize(self):
        num = (self.x**2 + self.y**2)**0.5
        self.x = self.x / num
        self.y = self.y / num

class Circle(pg.sprite.Sprite):
    def __init__(self, x, y, color, radius):
        super().__init__()
        self.image = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.color = color
        self.radius = radius
        self.x,self.y = x,y
        self.cross_x,self.cross_y = 0,0
        self.draw()

    def draw(self):
        self.image.fill((0, 0, 0, 0))
        pg.draw.circle(self.image, self.color,
                       (self.radius, self.radius),
                       self.radius)

    def update(self):
        self.x,self.y = pg.mouse.get_pos()
        self.rect.center = (self.x, self.y)

    def collision(self, Ax,Ay,Bx,By):
        AP = Vector(self.x-Ax,self.y-Ay)
        AB = Vector(Bx-Ax,By-Ay)
        AB.normalize()

        #単位ベクトルABとベクトルAPの内積(AXの距離)
        lenAX = AB.x*AP.x+AB.y*AP.y
        if lenAX < 0:
            #AXが負ならAPが最短距離
            shortest = ((Ax-self.x)**2 + (Ay-self.y)**2)**0.5
        elif lenAX > ((Ax-Bx)**2 + (Ay-By)**2)**0.5:
            #AXがABより長い場合はBPが最短距離
            shortest = ((Bx-self.x)**2 + (By-self.y)**2)**0.5
        else:
            #単位ベクトルAPとベクトルAPの外積(PXの距離)
            lenPX = AB.x*AP.y-AB.y*AP.x
            #PがAB線分上にあるので、PXが最短距離
            shortest = abs(lenPX)

        self.cross_x = Ax+(AB.x*lenAX)
        self.cross_y = Ay+(AB.y*lenAX)

        if shortest < self.radius:
            return True
        return False

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('線分と円の当たり判定')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Circle(30,30,(100,150,250),50)
all_sprites.add(player)

Ax = 150
Ay = 350
Bx = 350
By = 150
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    hit = False
    all_sprites.update()
    if player.collision(Ax,Ay,Bx,By):
        hit = True
        player.color = (255,0,0)
    else:
        player.color = (0,255,0)
    player.draw()

    screen.fill(pg.Color('white'))
    all_sprites.draw(screen)

    pg.draw.line(screen,(0,0,0),
                 (Ax,Ay),(Bx,By),3)
    if hit:
        pg.draw.circle(screen, (255,255,0),
                (player.cross_x,player.cross_y),5)

    pg.display.update()
    clock.tick(FPS)

pg.quit()
