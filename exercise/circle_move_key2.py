import pygame as pg

WIDTH, HEIGHT = 500, 500
FPS = 60
class Circle(pg.sprite.Sprite):
    def __init__(self,radius):
        super().__init__()
        self.image = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
        pg.draw.circle(self.image, (0,0,0), (radius, radius), radius)
        self.x, self.y = WIDTH/2, HEIGHT/2
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.radius = radius
        self.speed = 5

    def update(self):
        if self.x > WIDTH-self.radius:
            self.x = WIDTH-self.radius
        if self.x < self.radius:
            self.x = self.radius
        if self.y > HEIGHT-self.radius:
            self.y = HEIGHT-self.radius
        if self.y < self.radius:
            self.y = self.radius

        self.rect.center = (self.x, self.y)

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('円をキーで動かす')
clock = pg.time.Clock()

all_circles = pg.sprite.Group()
circle = Circle(25)
all_circles.add(circle)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                circle.y -= circle.speed
            if event.key == pg.K_DOWN:
                circle.y += circle.speed
            if event.key == pg.K_RIGHT:
                circle.x += circle.speed
            if event.key == pg.K_LEFT:
                circle.x -= circle.speed

    all_circles.update()
    screen.fill(pg.Color('white'))
    all_circles.draw(screen)

    pg.display.update()
    clock.tick(FPS)

pg.quit()
