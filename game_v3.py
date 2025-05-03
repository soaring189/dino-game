import pygame as p
import sys
import random
p.init()
screenSize = (600, 300)
screen = p.display.set_mode(screenSize)
bg = p.image.load("./Assets/bg.png").convert_alpha()
cloud_image = p.image.load("./Assets/cloud.png").convert_alpha()
dino0 = p.transform.scale(p.image.load("./Assets/dino-0.png").convert_alpha(), (45, 50))
dino1 = p.transform.scale(p.image.load("./Assets/dino-1.png").convert_alpha(), (45, 50))
dino2 = p.transform.scale(p.image.load("./Assets/dino-2.png").convert_alpha(), (45, 50))
dino0.set_colorkey((255, 255, 255))
dino1.set_colorkey((255, 255, 255))
dino2.set_colorkey((255, 255, 255))
dino_list = [dino0, dino1, dino2]
dino_state = 1
dino_x = 80
dino_y = 180
jump_speed = 1.4
is_jumping = False
count = 0
count1 = 0
modified_cloud = p.transform.scale(cloud_image, (70, 35))
cloud_position_list = [[600, random.randint(20, 150)], [600 + random.randint(100, 400), random.randint(20, 150)], [850 + random.randint(100, 400), random.randint(20, 150)]]
bgX = 0
bg2X = 600
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


def background(bgx, bg2x, bg_speed):
    bgx -= bg_speed * 0.7
    bg2x -= bg_speed * 0.7
    if bgx <= -600:
        bgx = 600
    if bg2x <= -600:
        bg2x = 600
    screen.blit(bg, (bgx, 200))
    screen.blit(bg, (bg2x, 200))
    return bgx, bg2x


def dino():
    global is_jumping, dino_y, jump_speed, dino_state, count, count1
    if p.key.get_pressed()[p.K_SPACE] and not is_jumping:
        is_jumping = True
    if is_jumping:
        dino_state = 0
        dino_y -= jump_speed
        jump_speed -= 0.007
        if dino_y > 181:
            dino_y = 180
            is_jumping = False
            jump_speed = 1.3
    if not is_jumping:
        if count1 % 80 == 0:
            dino_state = 2 if count % 2 == 0 else 1
            count += 1
    count1 += 1
    screen.blit(dino_list[dino_state], (dino_x, dino_y))


cloud1 = Cloud(cloud_position_list[0][0], cloud_position_list[0][1])
cloud2 = Cloud(cloud_position_list[1][0], cloud_position_list[1][1])
cloud3 = Cloud(cloud_position_list[2][0], cloud_position_list[2][1])
while True:
    screen.fill((255, 255, 255))
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
    bgX, bg2X = background(bgX, bg2X, speed)
    cloud1.update()
    cloud2.update()
    cloud3.update()
    dino()
    p.display.update()
    fps_clock.tick(FPS)
