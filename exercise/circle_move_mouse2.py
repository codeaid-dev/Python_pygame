import pygame as pg

WIDTH, HEIGHT = 500, 500
FPS = 60
class Circle(pg.sprite.Sprite):
    def __init__(self,radius,font):
        super().__init__()
        self.radius = radius
        self.font = font
        self.btninfo = 0
        self.mouse_state = (0, 0, 0)

        # 大きめのSurface（画面サイズ）を持つ
        self.image = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(0, 0))

    def update(self):
        # マウス座標取得
        mx, my = pg.mouse.get_pos()
        self.mouse_state = pg.mouse.get_pressed()

        # 毎フレーム描き直す
        self.image.fill((0, 0, 0, 0))  # 透明でクリア

        # ===== 円（マウスに追従）=====
        pg.draw.circle(self.image, (0, 0, 0), (mx, my), self.radius)

        # ===== テキスト（画面固定）=====
        b1, b2, b3 = self.mouse_state
        text = self.font.render(f"{b1}:{b2}:{b3}", True, pg.Color('red'))
        text2 = self.font.render(f'Button Info: {self.btninfo}', True, pg.Color('orange'))
        w, h = text.get_size()
        cx = (WIDTH - w) // 2
        cy = (HEIGHT - h) // 2
        self.image.blit(text, (cx, cy))
        self.image.blit(text2, (cx, cy + 30))

    def set_button(self, btn):
        self.btninfo = btn

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('マウスのボタンを取得する')
clock = pg.time.Clock()
font = pg.font.Font(None, 50)

all_circles = pg.sprite.Group()
circle = Circle(25, font)
all_circles.add(circle)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            circle.set_button(event.button)
        if event.type == pg.QUIT:
            running = False

    screen.fill(pg.Color('white'))

    all_circles.update()
    all_circles.draw(screen)

    pg.display.update()
    clock.tick(FPS)

pg.quit()
