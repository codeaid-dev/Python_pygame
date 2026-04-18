import pygame as pg, random

WIDTH, HEIGHT = 500, 500
FPS = 60
# ドローンのスプライトクラス
class Drone(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # 画像の作成 (ドローンの画像を読み込む)
        self.img = pg.image.load('images/drone_red.png')
        self.ow,self.oh = self.img.get_size()
        self.w,self.h = self.ow/5,self.oh/5
        self.x,self.y = x,y
        self.speed = [random.randint(-5, 5), random.randint(-5, 5)]
        self.growth = 1 # 大きさ変化量

        self.update_size()

    def update_size(self):
        self.image = pg.transform.scale(self.img, (self.w,self.h))
        # 位置の設定
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        # 移動処理
        self.rect.move_ip(self.speed)

        # 画面端での跳ね返り判定
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] *= -1
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH

        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed[1] *= -1
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT

        # 中央値更新
        self.x, self.y = self.rect.center

        # 大きさの変化
        self.w += self.growth
        self.h += self.growth
        if self.w > self.ow/2 or self.w < self.ow/5:
            self.growth *= -1

        self.update_size()

# メイン処理
pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('画像表示(テンプレート)')
clock = pg.time.Clock()

# グループの作成とスプライトの追加
all_drones = pg.sprite.Group()
drone = Drone(WIDTH/2,HEIGHT/2)
all_drones.add(drone)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # 一括更新
    # 全てのDroneのupdate()が実行される
    all_drones.update()

    # 一括描画
    screen.fill(pg.Color('white'))
    # 全てのDroneがscreenに描画される
    all_drones.draw(screen)

    pg.display.update()
    clock.tick(FPS)

pg.quit()
