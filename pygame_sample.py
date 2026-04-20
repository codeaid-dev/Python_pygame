import pygame as pg, sys, math

pg.init()
screen = pg.display.set_mode((800,600))
pg.display.set_caption('Sample')
font1 = pg.font.SysFont('meiryo', 50)
font2 = pg.font.SysFont(None, 50)
text1 = font1.render('あいうえお', True, (0,0,0))
text2 = font2.render('ABCDE', True, (0,0,0))
img = pg.image.load('images/neko.png')

while True:
    screen.fill(pg.Color('white'))
    pg.draw.rect(screen, pg.Color('red'), (100,100,50,150)) #四角形,座標：左上隅,横,縦
    pg.draw.rect(screen, pg.Color('red'), (160,100,50,150), 1) #width引数を指定すると塗りつぶしなし枠線あり
    pg.draw.line(screen, pg.Color('blue'), (250,100), (300,250), 5) #線,2点の座標
    pg.draw.circle(screen, pg.Color('green'), (400,175), 75) #円,座標：中心,半径
    pg.draw.circle(screen, pg.Color('green'), (560,175), 75, 5) #width引数を指定すると塗りつぶしなし枠線あり
    pg.draw.arc(screen, pg.Color('green'), (645,100,150,150), math.radians(90), math.radians(270), 5) # 円弧,座標：左上隅,横,縦
    pg.draw.ellipse(screen, (255,0,255), (100,270,50,150)) #楕円,座標：左上隅,横,縦
    pg.draw.ellipse(screen, (255,0,255), (160,270,50,150), 5) #width引数を指定すると塗りつぶしなし枠線あり
    pg.draw.polygon(screen, (0,255,255), [[245,270],[220,420],[270,420]]) #多角形,各点の座標リスト
    pg.draw.polygon(screen, (0,255,255), [[305,270],[280,420],[330,420]], 5) #width引数を指定すると塗りつぶしなし枠線あり
    pg.draw.polygon(screen, (255,255,0), [[335,420],[380,270],[440,270],[485,420]])
    pg.draw.polygon(screen, (255,255,0), [[495,420],[540,270],[600,270],[645,420]], 5)
    screen.blit(text1, (100,440)) #文字列,SysFontでフォント指定,renderで文字列と色指定,blitで表示,座標：左上隅
    screen.blit(text2, (360,440))
    screen.blit(img, (495,440)) #画像,loadで画像読み込み,blitで表示,座標：左上隅
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()