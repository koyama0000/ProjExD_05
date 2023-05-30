import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((1920, 1080))
# 画像の読み込み
background = pg.image.load("ex05/back.png")
slime = pg.image.load("ex05/slime.png")
window = pg.image.load("ex05/window.png")
#pg.image.frombuffer()
main_size = 2
main_window = pg.transform.scale(window, (window.get_width() * main_size, window.get_height() * main_size))
screen.blit(background, (0, 0))
screen.blit(slime, (760, 320))
screen.blit(window, (500, 780))
pg.display.flip()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            running = False
            pg.quit()