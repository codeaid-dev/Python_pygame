import pygame as pg, random

WIDTH, HEIGHT = 500, 500
FPS = 60
# 円のスプライトクラス
class Ball(pg.sprite.Sprite):
    def __init__(self, color, x, y, radius):
        super().__init__()
        # 位置と移動速度の設定
        self.speed = [random.randint(-5, 5), random.randint(-5, 5)]

        self.radius = radius # 半径設定
        self.x, self.y = x, y # 座標設定
        self.color = color # 色設定
        self.growth = 1 # 大きさ変化量

        self.update_size()

    def update_size(self):
        # 現在の半径に合わせて新しいSurfaceを作成
        size = self.radius * 2
        # 画像の作成 (透明な四角形の上に円を描く)
        self.image = pg.Surface((size, size), pg.SRCALPHA)
        pg.draw.circle(self.image, self.color,
                       (self.radius, self.radius), self.radius)
        # rect更新
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        # 移動処理
        self.rect.move_ip(self.speed)

        # 中央値更新
        self.x, self.y = self.rect.center

        # 画面端での跳ね返り判定
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed[1] *= -1

        # 大きさの変化
        self.radius += self.growth
        if self.radius > 50 or self.radius < 10:
            self.growth *= -1

        self.update_size()

# メイン処理
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('円を動かす(テンプレート)')
clock = pg.time.Clock()

# グループの作成とスプライトの追加
all_balls = pg.sprite.Group()
for _ in range(10):  # 10個の円を作成
    ball = Ball((random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255)),
                 WIDTH/2, HEIGHT/2, 20)
    all_balls.add(ball)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # 一括更新
    # 全てのBallのupdate()が実行される
    all_balls.update()

    # 一括描画
    screen.fill(pg.Color('white'))
    # 全てのBallがscreenに描画される
    all_balls.draw(screen)
    
    pg.display.update()
    clock.tick(FPS)

pg.quit()
