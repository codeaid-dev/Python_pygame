import pygame as pg, sys

WINDOW_SIZE = WIDTH,HEIGHT = 600,600
pg.init()
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption('スネークゲーム')

class Snake:
    def __init__(self):
        self.body = [[9,9] for i in range(5)]
        self.dx = 0
        self.dy = 0
    def direction(self,dx,dy):
        self.dx = dx
        self.dy = dy
    def move(self):
        for i in range(len(self.body)-1,0,-1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]
        self.body[0][0] += self.dx
        self.body[0][1] += self.dy
    def draw(self):
        for i in range(len(self.body)):
            rect = pg.Rect(self.body[i][0]*30,
                           self.body[i][1]*30,
                           30,30)
            pg.draw.rect(screen,(0,255,0),rect)
    def collision(self):
        return self.body[0][0] < 0 or \
            self.body[0][0] > 19 or \
            self.body[0][1] < 0 or \
            self.body[0][1] > 19

over = False
font = pg.font.SysFont('helvetica', 30)
snake = Snake()

while True:
    screen.fill(pg.Color('black'))
    if over:
        txt = font.render('GAME OVER',True,(255,0,0))
        screen.blit(txt,((WIDTH-txt.get_width())/2,
                        (HEIGHT-txt.get_height())/2))
    else:
        snake.move()
        snake.draw()
    if snake.collision():
        over = True

    pg.display.update()
    pg.time.Clock().tick(3)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                snake.direction(0,-1)
            if event.key == pg.K_DOWN:
                snake.direction(0,1)
            if event.key == pg.K_RIGHT:
                snake.direction(1,0)
            if event.key == pg.K_LEFT:
                snake.direction(-1,0)
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()