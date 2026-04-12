import pygame as pg
import sys

WINDOW_SIZE = WIDTH,HEIGHT = 800,450
BACKGROUND = (0,0,0)
FPS = 60

def main():
    pg.init()
    pg.display.set_caption("パックマンもどき")
    screen = pg.display.set_mode(WINDOW_SIZE)
    clock = pg.time.Clock()
    pac_man = [
        pg.image.load("images/pac-man0.png"),
        pg.image.load("images/pac-man1.png")
    ]
    tmr = 0

    while True:
        tmr += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F1:
                    screen = pg.display.set_mode(WINDOW_SIZE, pg.FULLSCREEN)
                if event.key == pg.K_F2 or event.key == pg.K_ESCAPE:
                    screen = pg.display.set_mode(WINDOW_SIZE)

        screen.fill(BACKGROUND)
        img = pac_man[(tmr//10)%2]
        rect = img.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(img,rect)
        pg.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
