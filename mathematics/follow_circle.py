import pygame as pg, math

WIDTH, HEIGHT = 500, 500
FPS = 60
class Circle(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.fx, self.fy = WIDTH-50, HEIGHT-50

    def update(self):
        mx,my = pg.mouse.get_pos()
        self.image.fill((0, 0, 0, 0))
        pg.draw.circle(self.image,(0,0,0),
                       (mx,my),5)
        self.draw_sin_cos(mx,my)
        self.follow_circle(mx,my)

    def draw_sin_cos(self,mx,my):
        pg.draw.line(self.image, (0,0,0),
                     (self.fx,self.fy),
                     (mx,my),1)
        pg.draw.line(self.image, (0,200,0),
                     (self.fx,self.fy),
                     (self.fx,my),5)
        pg.draw.line(self.image, (255,175,0),
                     (self.fx,self.fy),
                     (mx,self.fy),5)

    def show_degrees(self,radian):
        radian = (radian+2*math.pi)%(2*math.pi)
        degree = int(math.degrees(radian))
        font = pg.font.SysFont(None, 50)
        s1 = f'{degree:.0f} degrees'
        text1 = font.render(s1, True, (0,0,0))
        fw,fh = text1.get_size()
        self.image.blit(text1, (WIDTH/2-fw/2,HEIGHT/2+fh))
        s2 = f'{radian:.2f} radians'
        text2 = font.render(s2, True, (0,0,0))
        fw,fh = text2.get_size()
        self.image.blit(text2, (WIDTH/2-fw/2,HEIGHT/2+fh*2))

    def follow_circle(self,mx,my):
        dx = mx - self.fx
        dy = my - self.fy
        angle = math.atan2(dy,dx)
        dist = ((self.fx - mx)**2 + (self.fy - my)**2)**0.5
        if dist >= 1:
            self.fx += math.cos(angle)*2
            self.fy += math.sin(angle)*2
        pg.draw.circle(self.image, (255,0,0),
                       (self.fx,self.fy), 10)
        self.show_degrees(angle)

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('マウスについていく円')
clock = pg.time.Clock()

all_circles = pg.sprite.Group()
all_circles.add(Circle())

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
