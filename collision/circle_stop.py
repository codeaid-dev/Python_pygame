import pygame as pg, random

WIDTH, HEIGHT = 400, 400
FPS = 60
class Circle(pg.sprite.Sprite):
    def __init__(self, x, y, color, radius, is_player=False):
        super().__init__()
        self.speed = [random.randint(-5, 5), random.randint(-5, 5)]
        self.image = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.color = color
        self.radius = radius
        self.is_player = is_player
        self.stop = False
        self.draw()

    def draw(self):
        self.image.fill((0, 0, 0, 0))
        pg.draw.circle(self.image, self.color,
                       (self.radius, self.radius),
                       self.radius)

    def update(self,other):
        if self.is_player:
            mx,my = pg.mouse.get_pos()
            self.rect.center = (mx, my)
        elif other:
            if self.collision(other):
                self.stop = True
            else:
                if not self.stop:
                    self.rect.move_ip(self.speed)
                    if self.rect.left < 0 or self.rect.right > WIDTH:
                        self.speed[0] *= -1
                    if self.rect.top < 0 or self.rect.bottom > HEIGHT:
                        self.speed[1] *= -1

    def collision(self, other):
        dx = self.rect.centerx - other.rect.centerx
        dy = self.rect.centery - other.rect.centery
        distance = (dx**2 + dy**2)**0.5
        return distance <= (self.radius + other.radius)

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('円が当たったら止まる')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Circle(30,30,(100,150,250),30,True)
enemy = Circle(WIDTH/2,HEIGHT/2,(255,0,0),20)
all_sprites.add(player, enemy)

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
