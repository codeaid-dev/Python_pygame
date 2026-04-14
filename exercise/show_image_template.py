import pygame as pg

WIDTH, HEIGHT = 500, 500
FPS = 60
# ドローンのスプライトクラス
class Drone(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # 画像の作成 (ドローンの画像を読み込む)
        img = pg.image.load('images/drone_red.png')
        width,height = img.get_size()
        self.image = pg.transform.scale(img, (width/2,height/2))

        # 位置の設定
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        pass

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
