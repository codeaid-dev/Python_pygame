import pygame as pg, math

WIDTH, HEIGHT = 300, 300
FPS = 60
class Star(pg.sprite.Sprite):
    def __init__(self,x,y,radius1,radius2,num):
        super().__init__()
        self.image = pg.Surface((radius1*2,radius1*2), pg.SRCALPHA)
        vertices = []
        for i in range(num*2):
            if i%2 == 0:
                radius = radius1
            else:
                radius = radius2
            angle = math.radians(360/(num*2)*i-90)
            px = radius1 + radius * math.cos(angle)
            py = radius1 + radius * math.sin(angle)
            vertices.append([px,py])
        pg.draw.polygon(self.image, (255,255,0), vertices)
        pg.draw.polygon(self.image, (0,0,0), vertices,1)
        self.rect = self.image.get_rect(center=(x, y))

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('n芒星を描く')
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
all_sprites.add(Star(WIDTH/2,HEIGHT/2,100,40,5))

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
