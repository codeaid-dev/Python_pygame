import pygame as pg, sys, random

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
        for i in range(1,len(self.body)):
            if (self.dx != 0 or self.dy != 0) and \
                self.body[0][0] == self.body[i][0] and \
                self.body[0][1] == self.body[i][1]:
                return True
        return self.body[0][0] < 0 or \
            self.body[0][0] > 19 or \
            self.body[0][1] < 0 or \
            self.body[0][1] > 19
    def add_body(self):
        self.body.append([self.body[-1][0],
                          self.body[-1][1]])
    def eat(self,food):
        return self.body[0][0] == food.x \
            and self.body[0][1] == food.y

class Food:
    def draw(self):
        rect = pg.Rect(self.x*30,self.y*30,30,30)
        pg.draw.ellipse(screen,(255,0,0),rect)
    def set_position(self):
        self.x = random.randint(0,19)
        self.y = random.randint(0,19)

over = False
font = pg.font.SysFont('helvetica', 30)
snake = Snake()
food = Food()
food.set_position()

while True:
    screen.fill(pg.Color('black'))
    if over:
        txt = font.render('GAME OVER',True,(255,0,0))
        screen.blit(txt,((WIDTH-txt.get_width())/2,
                        (HEIGHT-txt.get_height())/2))
    else:
        food.draw()
        snake.move()
        snake.draw()
    if snake.collision():
        over = True
    if snake.eat(food):
        snake.add_body()
        food.set_position()

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