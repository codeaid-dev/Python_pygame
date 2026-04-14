import pygame as pg, sys

WIDTH, HEIGHT = 500, 500
FPS = 60
pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('画像拡大縮小')
clock = pg.time.Clock()
img = pg.image.load('images/drone_red.png')
width,height = img.get_size()
#img = pg.transform.scale(img,(width/2,height/2))
#img = pg.transform.scale(img,(width*1.5,height*1.5))
#width,height = img.get_size()

while True:
    screen.fill(pg.Color('white'))
    screen.blit(img, ((WIDTH-width)/2,(HEIGHT-height)/2))
    pg.display.update()
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()