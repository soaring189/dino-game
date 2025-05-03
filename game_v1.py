import pygame as p
import sys
p.init()
screenSize = (600, 300)
screen = p.display.set_mode(screenSize)
bg = p.image.load("./Assets/bg.png").convert_alpha()
bgX = 0
bg2X = 600
fps_clock = p.time.Clock()
FPS = 600
speed = 0.7


def background(bgx, bg2x):
    screen.blit(bg, (bgx, 200))
    screen.blit(bg, (bg2x, 200))


while True:
    screen.fill((255, 255, 255))
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
    bgX -= speed
    bg2X -= speed
    if bgX <= -600:
        bgX = 600
    if bg2X <= -600:
        bg2X = 600
    background(bgX, bg2X)
    p.display.update()
    fps_clock.tick(FPS)
