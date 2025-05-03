import pygame as p
import sys
import random
p.init()
screenSize = (600, 300)
screen = p.display.set_mode(screenSize)
bg = p.image.load("./Assets/bg.png").convert_alpha()
cloud_image = p.image.load("./Assets/cloud.png").convert_alpha()
modified_cloud = p.transform.scale(cloud_image, (70, 35))
bgX = 0
bg2X = 600
cloud_position_list = [[600, random.randint(20, 150)], [600 + random.randint(100, 400), random.randint(20, 150)], [850 + random.randint(100, 400), random.randint(20, 150)]]
fps_clock = p.time.Clock()
FPS = 600
speed = 1


class Cloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        self.x -= speed*0.1
        if self.x < -100:
            self.x = random.randint(700, 850)
            self.y = random.randint(20, 150)
        screen.blit(modified_cloud, (self.x, self.y))


def background(bgx, bg2x):
    screen.blit(bg, (bgx, 200))
    screen.blit(bg, (bg2x, 200))


cloud1 = Cloud(cloud_position_list[0][0], cloud_position_list[0][1])
cloud2 = Cloud(cloud_position_list[1][0], cloud_position_list[1][1])
cloud3 = Cloud(cloud_position_list[2][0], cloud_position_list[2][1])
while True:
    screen.fill((255, 255, 255))
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
    bgX -= speed*0.7
    bg2X -= speed*0.7
    if bgX <= -600:
        bgX = 600
    if bg2X <= -600:
        bg2X = 600
    background(bgX, bg2X)
    cloud1.update()
    cloud2.update()
    cloud3.update()
    p.display.update()
    fps_clock.tick(FPS)
