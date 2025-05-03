import pygame as p
import sys
import random
import ctypes
from ctypes import wintypes
p.init()
screenSize = (600, 300)
screen = p.display.set_mode(screenSize)
hwnd = p.display.get_wm_info()["window"]
p.display.set_caption("dino game")
bg = p.image.load("./Assets/bg.png").convert_alpha()
cloud_image = p.transform.scale(p.image.load("./Assets/cloud.png").convert_alpha(), (70, 35))
cloud_night_image = p.transform.scale(p.image.load("./Assets/cloud-night.png").convert_alpha(), (70, 35))
star0 = p.image.load("./Assets/star-0.png").convert_alpha()
star1 = p.image.load("./Assets/star-1.png").convert_alpha()
moon = p.image.load("./Assets/moon.png").convert_alpha()
game_over_image = p.image.load("./Assets/GameOver.png").convert_alpha()
HI = p.transform.scale(p.image.load("./Assets/HI.png").convert_alpha(), (24, 13))
restart = p.transform.scale(p.image.load("./Assets/restart.png").convert_alpha(), (43.57, 39.29))
cactus0 = p.transform.scale(p.image.load("./Assets/cactus-0.png").convert_alpha(), (18.67, 41.33))
cactus1 = p.transform.scale(p.image.load("./Assets/cactus-1.png").convert_alpha(), (28.67, 57.33))
cactus2 = p.transform.scale(p.image.load("./Assets/cactus-2.png").convert_alpha(), (42, 43.33))
cactus3 = p.transform.scale(p.image.load("./Assets/cactus-3.png").convert_alpha(), (64, 43.33))
cactus4 = p.transform.scale(p.image.load("./Assets/cactus-4.png").convert_alpha(), (95.33, 62))
pterosaur0 = p.transform.scale(p.image.load("./Assets/pterosaur-0.png").convert_alpha(), (42, 30))
pterosaur1 = p.transform.scale(p.image.load("./Assets/pterosaur-1.png").convert_alpha(), (42, 26))
dino0 = p.transform.scale(p.image.load("./Assets/dino-0.png").convert_alpha(), (45, 50))
dino1 = p.transform.scale(p.image.load("./Assets/dino-1.png").convert_alpha(), (45, 50))
dino2 = p.transform.scale(p.image.load("./Assets/dino-2.png").convert_alpha(), (45, 50))
dino3 = p.transform.scale(p.image.load("./Assets/dino-3.png").convert_alpha(), (45, 50))
dino4 = p.transform.scale(p.image.load("./Assets/dino-4.png").convert_alpha(), (60, 30))
dino5 = p.transform.scale(p.image.load("./Assets/dino-5.png").convert_alpha(), (60, 30))
dino_x = 80
dino_y = 180
dino_list = [dino0, dino1, dino2, dino3, dino4, dino5]
dino_state = 1
dino_mask = p.mask.from_surface(dino_list[dino_state])
jump_speed = 1.4
is_jumping = False
count = 0
count1 = 0
pterosaur_state = 0
cloud_position_list = [[600, random.randint(20, 150)], [600 + random.randint(100, 400), random.randint(20, 150)], [850 + random.randint(100, 400), random.randint(20, 150)]]
bgX = 0
bg2X = 600
star0X = random.randint(100, 400)
star0Y = random.randint(20, 150)
star1X = 200 + random.randint(100, 400)
star1Y = random.randint(20, 150)
moonX = 450 + random.randint(100, 200)
moonY = random.randint(20, 100)
pterosaur_y = random.choice([140, 165, 190])
which_barrier = random.randint(0, 4)
cactus_list = [cactus0, cactus1, cactus2, cactus3, cactus4]
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
is_day = True
switch_cooldown = 100
day_night_switch_state = False
bg_colour = 255
bg_day, bg_night = None, None
cloud_day, cloud_night = None, None
game_over_day, game_over_night = None, None
HI_day, HI_night = None, None
restart_day, restart_night = None, None
cactus_day, cactus_night = None, None
pterosaur0_day, pterosaur0_night = None, None
pterosaur1_day, pterosaur1_night = None, None
dino_day, dino_night = None, None
bright_number_list_day, bright_number_list_night = None, None
dark_number_list_day, dark_number_list_night = None, None
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
        screen.blit(cloud_image, (self.x, self.y))


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


def night():
    global star0X, star0Y, star1X, star1Y, moonX, moonY
    if not is_day:
        screen.blit(star0, (star0X, star0Y))
        screen.blit(star1, (star1X, star1Y))
        screen.blit(moon, (moonX, moonY))
    if star0X < -20:
        star0X = 600 + random.randint(100, 400)
        star0Y = random.randint(20, 150)
    if star1X < -20:
        star1X = 600 + random.randint(100, 400)
        star1Y = random.randint(20, 150)
    if moonX < -20:
        moonX = 600 + random.randint(100, 400)
        moonY = random.randint(20, 100)
    if gaming:
        star0X -= 0.1*speed
        star1X -= 0.1 * speed
        if not is_day:
            moonX -= 0.043 * speed


def dino():
    global is_jumping, dino_y, jump_speed, dino_state, count, count1
    if gaming:
        if (p.key.get_pressed()[p.K_SPACE] or p.key.get_pressed()[p.K_UP]) and not is_jumping:
            is_jumping = True
        if is_jumping:
            dino_state = 0
            dino_y -= jump_speed
            if p.key.get_pressed()[p.K_DOWN]:
                jump_speed -= 0.012
            else:
                jump_speed -= 0.007
            if dino_y > 181:
                dino_y = 180
                is_jumping = False
                jump_speed = 1.3
        if not is_jumping:
            if p.key.get_pressed()[p.K_DOWN]:
                dino_y = 200
                dino_state = 4 if count % 2 == 0 else 5
            else:
                dino_y = 180
                dino_state = 1 if count % 2 == 0 else 2
            if count1 % 80 == 0:
                count += 1

        count1 += 1
    else:
        if dino_y > 181:
            dino_y = 180
        dino_state = 3

    screen.blit(dino_list[dino_state], (dino_x, dino_y))


def barrier():
    global which_barrier, cactus_list, barrier_x, speed, gaming, pterosaur_state, pterosaur_y
    if gaming:
        barrier_x -= speed
        pterosaur_state += 0.002
    if which_barrier == 0:
        barrier_y = 193
    elif which_barrier == 1:
        barrier_y = 173
    elif which_barrier in [2, 3]:
        barrier_y = 185
    elif which_barrier == 4:
        barrier_y = 168
    else:
        barrier_y = pterosaur_y
    if which_barrier in [0, 1, 2, 3, 4]:
        barrier_rect = cactus_list[which_barrier].get_rect(topleft=(barrier_x, barrier_y))
        barrier_mask = p.mask.from_surface(cactus_list[which_barrier])
        offset = (barrier_rect.x - dino_x, barrier_rect.y - dino_y)
        screen.blit(cactus_list[which_barrier], barrier_rect.topleft)
    else:
        if int(pterosaur_state) % 2 == 0:
            barrier_rect = pterosaur0.get_rect(topleft=(barrier_x, barrier_y))
            barrier_mask = p.mask.from_surface(pterosaur0)
            offset = (barrier_rect.x - dino_x, barrier_rect.y - dino_y)
            screen.blit(pterosaur0, (barrier_x, barrier_y))
        else:
            barrier_rect = pterosaur1.get_rect(topleft=(barrier_x, barrier_y-6))
            barrier_mask = p.mask.from_surface(pterosaur1)
            offset = (barrier_rect.x - dino_x, barrier_rect.y - dino_y)
            screen.blit(pterosaur1, (barrier_x, barrier_y-6))
    if dino_mask.overlap(barrier_mask, offset):
        gaming = False
    if barrier_x < -96:
        barrier_x = 600
        pterosaur_y = random.choice([140, 165, 190])
        which_barrier = random.randint(0, 5)
        speed += 0.01


def reset():
    global cloud_position_list, star0X, star0Y, star1X, star1Y, moonX, moonY, speed, dino_x, dino_y, jump_speed, is_jumping, count, count1, which_barrier, barrier_x, gaming, score, restart_delay, is_day, bgX, bg2X
    score = 0
    bgX = 0
    bg2X = 600
    cloud_position_list = [[600, random.randint(20, 150)], [600 + random.randint(100, 400), random.randint(20, 150)], [850 + random.randint(100, 400), random.randint(20, 150)]]
    star0X = random.randint(100, 400)
    star0Y = random.randint(20, 150)
    star1X = 200 + random.randint(100, 400)
    star1Y = random.randint(20, 150)
    moonX = 450 + random.randint(100, 200)
    speed = 1
    dino_x = 80
    dino_y = 180
    count = 0
    count1 = 0
    which_barrier = random.randint(0, 4)
    barrier_x = 1000
    is_day = True
    p.display.set_icon(dino0)
    try:
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 20, ctypes.byref(
            wintypes.BOOL(0)), ctypes.sizeof(wintypes.BOOL))
    except Exception as e:
        print(e)
    gaming = True
    restart_delay = 0


def display_score():
    global score, highest_score
    if gaming:
        score += 0.014 * speed
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


def invert_colors(surface):
    inverted_surface = surface.copy()
    for image_x in range(surface.get_width()):
        for image_y in range(surface.get_height()):
            r, g, b, a = surface.get_at((image_x, image_y))
            inverted_surface.set_at((image_x, image_y), (255 - r, 255 - g, 255 - b, a))
    return inverted_surface


def precompute_image():
    global bg, cloud_image, game_over_image, HI, restart, cactus0, cactus1, cactus2, cactus3, cactus4, pterosaur0_day, pterosaur0_night, pterosaur1_day, pterosaur1_night, dino_list, bright_number_list, dark_number_list, bg_day, bg_night, cloud_day, cloud_night, game_over_day, game_over_night, HI_day, HI_night, restart_day, restart_night, cactus_day, cactus_night, dino_day, dino_night, bright_number_list_day, bright_number_list_night, dark_number_list_day, dark_number_list_night
    bg_day, bg_night = bg.copy(), invert_colors(bg)
    cloud_day, cloud_night = cloud_image.copy(), cloud_night_image
    game_over_day, game_over_night = game_over_image.copy(), invert_colors(game_over_image)
    HI_day, HI_night = HI.copy(), invert_colors(HI)
    restart_day, restart_night = restart.copy(), invert_colors(restart)
    cactus_day = [cactus0.copy(), cactus1.copy(), cactus2.copy(), cactus3.copy(), cactus4.copy()]
    cactus_night = [invert_colors(cactus0), invert_colors(cactus1), invert_colors(cactus2), invert_colors(cactus3), invert_colors(cactus4)]
    pterosaur0_day, pterosaur0_night = pterosaur0.copy(), invert_colors(pterosaur0)
    pterosaur1_day, pterosaur1_night = pterosaur1.copy(), invert_colors(pterosaur1)
    dino_day = [d.copy() for d in dino_list]
    dino_night = [invert_colors(d) for d in dino_list]
    bright_number_list_day = [n.copy() for n in bright_number_list]
    bright_number_list_night = [invert_colors(n) for n in bright_number_list]
    dark_number_list_day = [n.copy() for n in dark_number_list]
    dark_number_list_night = [invert_colors(n) for n in dark_number_list]


def day_night():
    global score, switch_cooldown, day_night_switch_state, is_day, moonX, bg_colour, bg, cloud_image, game_over_image, HI, restart, cactus_list, pterosaur0, pterosaur1, dino_list, bright_number_list, dark_number_list
    if int(score) > 0 and int(score) % 200 == 0 and switch_cooldown > 100:
        is_day = not is_day
        if is_day:
            moonX = 450 + random.randint(100, 200)
            try:
                ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 20, ctypes.byref(wintypes.BOOL(0)), ctypes.sizeof(wintypes.BOOL))
            except Exception as e:
                print(e)
            p.display.set_icon(dino0)
        else:
            try:
                ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 20, ctypes.byref(wintypes.BOOL(1)), ctypes.sizeof(wintypes.BOOL))
            except Exception as e:
                print(e)
            p.display.set_icon(invert_colors(dino0))
        switch_cooldown = 0
    switch_cooldown += 1
    if is_day:
        if bg_colour < 255:
            bg_colour += 1
        if day_night_switch_state:
            day_night_switch_state = False
    else:
        if bg_colour > 0:
            bg_colour -= 1
        if not day_night_switch_state:
            day_night_switch_state = True
    screen.fill((bg_colour, bg_colour, bg_colour))
    bg = bg_day if is_day else bg_night
    cloud_image = cloud_day if is_day else cloud_night
    game_over_image = game_over_day if is_day else game_over_night
    HI = HI_day if is_day else HI_night
    restart = restart_day if is_day else restart_night
    cactus_list = cactus_day if is_day else cactus_night
    pterosaur0 = pterosaur0_day if is_day else pterosaur0_night
    pterosaur1 = pterosaur1_day if is_day else pterosaur1_night
    dino_list = dino_day if is_day else dino_night
    bright_number_list = bright_number_list_day if is_day else bright_number_list_night
    dark_number_list = dark_number_list_day if is_day else dark_number_list_night


def game_over():
    global restart_delay
    if not gaming:
        screen.blit(game_over_image, (140, 90))
        restart_delay += 1
        if restart_delay > 300:
            screen.blit(restart, (270, 150))
            if p.key.get_pressed()[p.K_SPACE] or p.key.get_pressed()[p.K_UP]:
                reset()


precompute_image()
cloud1 = Cloud(cloud_position_list[0][0], cloud_position_list[0][1])
cloud2 = Cloud(cloud_position_list[1][0], cloud_position_list[1][1])
cloud3 = Cloud(cloud_position_list[2][0], cloud_position_list[2][1])
while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
    day_night()
    night()
    bgX, bg2X = background(bgX, bg2X, speed)
    cloud1.update()
    cloud2.update()
    cloud3.update()
    barrier()
    dino()
    display_score()
    game_over()
    p.display.update()
    fps_clock.tick(FPS)
