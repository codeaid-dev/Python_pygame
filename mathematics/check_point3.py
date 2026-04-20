import pygame as pg, math

WIDTH, HEIGHT = 500, 500
FPS = 60
class Circle(pg.sprite.Sprite):
    def __init__(self,radius):
        super().__init__()
        self.image = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.radius = radius

    def update(self):
        mx,my = pg.mouse.get_pos()
        self.image.fill((0, 0, 0, 0))
        self.draw_guid()
        angle = math.atan2(my-HEIGHT/2, mx-WIDTH/2)
        x = (WIDTH/2)+200*math.cos(angle)
        y = (HEIGHT/2)+200*math.sin(angle)
        degree = ((angle+2*math.pi)%(2*math.pi)) * 180 / math.pi
        pg.draw.arc(self.image, (0,0,0),
                    (WIDTH/2-25,HEIGHT/2-25,50,50),
                    math.radians(-degree),
                    math.radians(0), 1)
        font = pg.font.SysFont(None, 50)
        s1 = f'{degree:.0f} degrees'
        text1 = font.render(s1, True, (0,0,0))
        fw,fh = text1.get_size()
        self.image.blit(text1, (WIDTH/2-fw/2,HEIGHT/2+fh))
        s2 = f'{math.radians(degree):.2f} radians'
        text2 = font.render(s2, True, (0,0,0))
        fw,fh = text2.get_size()
        self.image.blit(text2, (WIDTH/2-fw/2,HEIGHT/2+fh*2))
        pg.draw.line(self.image, (0,0,0),
                     (WIDTH/2,HEIGHT/2),
                     (x,y), 2)
        pg.draw.circle(self.image, (0, 0, 0),
                       (x, y), self.radius)
        self.draw_sin_cos(x,y)

    def draw_guid(self):
        pg.draw.circle(self.image, (200,200,200),
                       (WIDTH/2,HEIGHT/2), 200, 1)
        pg.draw.line(self.image, (200,200,200),
                     (WIDTH/2-200,HEIGHT/2),
                     (WIDTH/2+200,HEIGHT/2), 1)
        pg.draw.line(self.image, (200,200,200),
                     (WIDTH/2,HEIGHT/2-200),
                     (WIDTH/2,HEIGHT/2+200), 1)
    
    def draw_sin_cos(self,x,y):
        pg.draw.line(self.image, (0,200,0),
                     (WIDTH/2,HEIGHT/2),
                     (WIDTH/2,y), 3)
        pg.draw.line(self.image, (255,175,0),
                     (WIDTH/2,HEIGHT/2),
                     (x,HEIGHT/2), 3)

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('円周上の座標')
clock = pg.time.Clock()

all_circles = pg.sprite.Group()
all_circles.add(Circle(5))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_circles.update()
    screen.fill(pg.Color('white'))
    all_circles.draw(screen)

    pg.display.update()
    clock.tick(FPS)

pg.quit()
