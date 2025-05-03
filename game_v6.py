import pygame as p
import sys
import random
p.init()
screenSize = (600, 300)
screen = p.display.set_mode(screenSize)
p.display.set_caption("dino game")
bg = p.image.load("./Assets/bg.png").convert_alpha()
cloud_image = p.image.load("./Assets/cloud.png").convert_alpha()
game_over = p.image.load("./Assets/GameOver.png").convert_alpha()
HI = p.transform.scale(p.image.load("./Assets/HI.png").convert_alpha(), (24, 13))
restart = p.transform.scale(p.image.load("./Assets/restart.png").convert_alpha(), (43.57, 39.29))
cactus0 = p.transform.scale(p.image.load("./Assets/cactus-0.png").convert_alpha(), (18.67, 41.33))
cactus1 = p.transform.scale(p.image.load("./Assets/cactus-1.png").convert_alpha(), (28.67, 57.33))
cactus2 = p.transform.scale(p.image.load("./Assets/cactus-2.png").convert_alpha(), (42, 43.33))
cactus3 = p.transform.scale(p.image.load("./Assets/cactus-3.png").convert_alpha(), (64, 43.33))
cactus4 = p.transform.scale(p.image.load("./Assets/cactus-4.png").convert_alpha(), (95.33, 62))
dino0 = p.transform.scale(p.image.load("./Assets/dino-0.png").convert_alpha(), (45, 50))
dino1 = p.transform.scale(p.image.load("./Assets/dino-1.png").convert_alpha(), (45, 50))
dino2 = p.transform.scale(p.image.load("./Assets/dino-2.png").convert_alpha(), (45, 50))
dino3 = p.transform.scale(p.image.load("./Assets/dino-3.png").convert_alpha(), (45, 50))
rect_cactus0 = cactus0.get_rect()
rect_cactus1 = cactus1.get_rect()
rect_cactus2 = cactus2.get_rect()
rect_cactus3 = cactus3.get_rect()
rect_cactus4 = cactus4.get_rect()
dino_x = 80
dino_y = 180
rect_dino0 = p.Rect(dino_x, dino_y, 45, 50)
rect_dino0.height -= 10
rect_dino0.width -= 10
rect_dino1 = dino0.get_rect()
rect_dino2 = dino0.get_rect()
dino0.set_colorkey((255, 255, 255))
dino1.set_colorkey((255, 255, 255))
dino2.set_colorkey((255, 255, 255))
dino_list = [dino0, dino1, dino2, dino3]
dino_state = 1
jump_speed = 1.4
is_jumping = False
count = 0
count1 = 0
modified_cloud = p.transform.scale(cloud_image, (70, 35))
cloud_position_list = [[600, random.randint(20, 150)], [600 + random.randint(100, 400), random.randint(20, 150)], [850 + random.randint(100, 400), random.randint(20, 150)]]
bgX = 0
bg2X = 600
which_barrier = random.randint(0, 5)
barrier_x = 600
bright_number_list = []
dark_number_list = []
score = 0
highest_score = 0
for i in range(0, 10):
    number = p.image.load(f"./Assets/{i}.png").convert_alpha()
    modified_number = p.transform.scale(p.image.load(f"./Assets/{i}.png").convert_alpha(), (11, 13))
    bright_number = modified_number.copy()
    dark_number = modified_number.copy()
    for x in range(modified_number.get_width()):
        for y in range(modified_number.get_height()):
            color = modified_number.get_at((x, y))
            if color != (255, 255, 255, 0):
                bright_number.set_at((x, y), (120, 120, 120))
                dark_number.set_at((x, y), (90, 90, 90))
    bright_number_list.append(bright_number)
    dark_number_list.append(dark_number)
for x in range(HI.get_width()):
    for y in range(HI.get_height()):
        color = HI.get_at((x, y))
        if color != (255, 255, 255, 0):
            HI.set_at((x, y), (120, 120, 120))
p.display.set_icon(dino0)
fps_clock = p.time.Clock()
FPS = 600
speed = 0.7
gaming = True
restart_delay = 0


class Cloud:
    def __init__(self, cloud_x, cloud_y):
        self.x = cloud_x
        self.y = cloud_y

    def update(self):
        if gaming:
            self.x -= speed*0.1
            if self.x < -100:
                self.x = random.randint(700, 850)
                self.y = random.randint(20, 150)
        screen.blit(modified_cloud, (self.x, self.y))


def background(bgx, bg2x, bg_speed):
    if gaming:
        bgx -= bg_speed
        bg2x -= bg_speed
        if bgx <= -600:
            bgx = 600
        if bg2x <= -600:
            bg2x = 600
    screen.blit(bg, (bgx, 200))
    screen.blit(bg, (bg2x, 200))
    return bgx, bg2x


def dino():
    global is_jumping, dino_y, jump_speed, dino_state, count, count1
    if gaming:
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
    else:
        dino_state = 3
    screen.blit(dino_list[dino_state], (dino_x, dino_y))


def rect_update():
    rect_dino0.x = dino_x
    rect_dino0.y = dino_y
    rect_dino1.x = dino_x
    rect_dino1.y = dino_y
    rect_dino2.x = dino_x
    rect_dino2.y = dino_y
    rect_cactus0.x = barrier_x
    rect_cactus0.y = 193
    rect_cactus1.x = barrier_x
    rect_cactus1.y = 173
    rect_cactus2.x = barrier_x
    rect_cactus2.y = 185
    rect_cactus3.x = barrier_x
    rect_cactus3.y = 185
    rect_cactus4.x = barrier_x
    rect_cactus4.y = 170


def barrier():
    global which_barrier, barrier_x, speed, gaming
    if gaming:
        barrier_x -= speed
    if which_barrier == 0:
        screen.blit(cactus0, (barrier_x, 193))
        if rect_cactus0.colliderect(rect_dino0) or rect_cactus0.colliderect(rect_dino1) or rect_cactus0.colliderect(rect_dino2):
            gaming = False
    elif which_barrier == 1:
        screen.blit(cactus1, (barrier_x, 173))
        if rect_cactus1.colliderect(rect_dino0) or rect_cactus0.colliderect(rect_dino1) or rect_cactus0.colliderect(rect_dino2):
            gaming = False
    elif which_barrier == 2:
        screen.blit(cactus2, (barrier_x, 185))
        if rect_cactus2.colliderect(rect_dino0) or rect_cactus0.colliderect(rect_dino1) or rect_cactus0.colliderect(rect_dino2):
            gaming = False
    elif which_barrier == 3:
        screen.blit(cactus3, (barrier_x, 185))
        if rect_cactus3.colliderect(rect_dino0) or rect_cactus0.colliderect(rect_dino1) or rect_cactus0.colliderect(rect_dino2):
            gaming = False
    elif which_barrier == 4:
        screen.blit(cactus4, (barrier_x, 168))
        if rect_cactus4.colliderect(rect_dino0) or rect_cactus0.colliderect(rect_dino1) or rect_cactus0.colliderect(rect_dino2):
            gaming = False
    if barrier_x < -96:
        barrier_x = 600
        which_barrier = random.randint(0, 5)
        speed += 0.01


def reset():
    global cloud_position_list, speed, dino_x, dino_y, jump_speed, is_jumping, count, count1, which_barrier, barrier_x, gaming, score, restart_delay
    score = 0
    cloud_position_list = [[600, random.randint(20, 150)], [600 + random.randint(100, 400), random.randint(20, 150)], [850 + random.randint(100, 400), random.randint(20, 150)]]
    speed = 1
    dino_x = 80
    dino_y = 180
    count = 0
    count1 = 0
    which_barrier = random.randint(0, 5)
    barrier_x = 1000
    gaming = True
    restart_delay = 0


def display_score():
    global score, highest_score
    if gaming:
        score += 0.014
    screen.blit(dark_number_list[int(score) % 10], (560, 15))
    screen.blit(dark_number_list[(int(score) // 10) % 10], (547, 15))
    screen.blit(dark_number_list[(int(score) // 100) % 10], (534, 15))
    screen.blit(dark_number_list[(int(score) // 1000) % 10], (521, 15))
    screen.blit(dark_number_list[(int(score) // 10000) % 10], (508, 15))
    if score > highest_score:
        highest_score = score
    screen.blit(bright_number_list[int(highest_score) % 10], (478, 15))
    screen.blit(bright_number_list[(int(highest_score) // 10) % 10], (465, 15))
    screen.blit(bright_number_list[(int(highest_score) // 100) % 10], (452, 15))
    screen.blit(bright_number_list[(int(highest_score) // 1000) % 10], (439, 15))
    screen.blit(bright_number_list[(int(highest_score) // 10000) % 10], (426, 15))
    screen.blit(HI, (390, 15))


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
    rect_update()
    cloud1.update()
    cloud2.update()
    cloud3.update()
    barrier()
    dino()
    display_score()
    if not gaming:
        screen.blit(game_over, (140, 90))
        screen.blit(restart, (270, 150))
        restart_delay += 1
        if restart_delay > 300:
            if p.key.get_pressed()[p.K_SPACE]:
                reset()
    p.display.update()
    fps_clock.tick(FPS)
