import pygame as pg
import os
import math
import random

pg.mixer.init()
pg.font.init()

pg.init()

WIDTH = 900
HEIGHT = 500

METEOR_WIDTH,METEOR_HEIGHT = 50,50

METEOR_VEL = 2

METEOR_1_DIR = random.randint(0, 359)
METEOR_2_DIR = random.randint(0, 359)
METEOR_3_DIR = random.randint(0, 359)
METEOR_1_X_VEL = math.cos(METEOR_1_DIR) * METEOR_VEL
METEOR_1_Y_VEL = math.sin(METEOR_1_DIR) * METEOR_VEL
METEOR_2_X_VEL = math.cos(METEOR_2_DIR) * METEOR_VEL
METEOR_2_Y_VEL = math.sin(METEOR_2_DIR) * METEOR_VEL
METEOR_3_X_VEL = math.cos(METEOR_3_DIR) * METEOR_VEL
METEOR_3_Y_VEL = math.sin(METEOR_3_DIR) * METEOR_VEL

METEOR_IMAGE = pg.image.load(os.path.join('Assets', 'meteor.png'))

METEOR_1 = pg.transform.rotate(pg.transform.scale(METEOR_IMAGE, (METEOR_WIDTH, METEOR_HEIGHT)), 90)
METEOR_2 = pg.transform.rotate(pg.transform.scale(METEOR_IMAGE, (METEOR_WIDTH, METEOR_HEIGHT)), 90)
METEOR_3 = pg.transform.rotate(pg.transform.scale(METEOR_IMAGE, (METEOR_WIDTH, METEOR_HEIGHT)), 90)

WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Star wars")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

BACKGROUND = pg.transform.scale(pg.image.load(os.path.join('Assets', 'space.png')), (WIDTH,HEIGHT))

BULLET_HIT_SOUND = pg.mixer.Sound(os.path.join('Assets', 'explosion.wav'))
BULLET_FIRE_SOUND = pg.mixer.Sound(os.path.join('Assets', 'laser.wav'))

HEALTH_FONT = pg.font.SysFont('arial', 40)
WINNER_FONT = pg.font.SysFont('algerian', 100)

FPS = 60
VELOCITY = 5
BULLET_VEL = 7
MAX_BULLETS = 3

SPACESHIP_WIDTH = 80
SPACESHIP_HEIGHT = 60

YELLOW_HIT = pg.USEREVENT + 1
RED_HIT = pg.USEREVENT + 2

YELLOW_SPACESHIP_IMG = pg.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMG = pg.image.load(os.path.join('Assets', 'spaceship_red.png'))

YELLOW_SPACESHIP = pg.transform.rotate(pg.transform.scale(YELLOW_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP = pg.transform.rotate(pg.transform.scale(RED_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

BORDER = pg.Rect(WIDTH // 2-5, 0, 10, HEIGHT)


def yellow_control(key_pressed, yellow):
    if key_pressed[pg.K_a] and yellow.x - VELOCITY - yellow.width > -15:
        yellow.x -= VELOCITY
    if key_pressed[pg.K_d] and yellow.x + VELOCITY + yellow.width < BORDER.x:
        yellow.x += VELOCITY
    if key_pressed[pg.K_w] and yellow.y - VELOCITY - yellow.height > -10:
        yellow.y -= VELOCITY
    if key_pressed[pg.K_s] and yellow.y + VELOCITY + yellow.width < HEIGHT:
        yellow.y += VELOCITY


def red_control(key_pressed, red):
    if key_pressed[pg.K_LEFT] and red.x - VELOCITY - red.width > BORDER.x:
        red.x -= VELOCITY
    if key_pressed[pg.K_RIGHT] and red.x + VELOCITY + red.width < WIDTH:
        red.x += VELOCITY
    if key_pressed[pg.K_UP] and red.y - VELOCITY - red.height > -15:
        red.y -= VELOCITY
    if key_pressed[pg.K_DOWN] and red.y + red.height + VELOCITY < HEIGHT:
        red.y += VELOCITY


def draw_window(red, yellow, red_health, yellow_health, red_bullets, yellow_bullets, meteor1, meteor2, meteor3):
    WINDOW.blit(BACKGROUND, (0,0))
    pg.draw.rect(WINDOW, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), True, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), True, WHITE)

    WINDOW.blit(red_health_text, (WIDTH-red_health_text.get_width()-10,10))
    WINDOW.blit(yellow_health_text, (10, 10))

    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))

    WINDOW.blit(METEOR_1, (meteor1.x, meteor1.y))
    WINDOW.blit(METEOR_2, (meteor2.x, meteor2.y))
    WINDOW.blit(METEOR_3, (meteor3.x, meteor3.y))

    for bullet in red_bullets:
        pg.draw.rect(WINDOW, RED, bullet)

    for bullet in yellow_bullets:
        pg.draw.rect(WINDOW, YELLOW, bullet)

    pg.display.update()


def meteor_controller(meteor1, meteor2, meteor3):
    meteor1.x += METEOR_1_X_VEL
    meteor1.y += METEOR_1_Y_VEL
    meteor2.x += METEOR_2_X_VEL
    meteor2.y += METEOR_2_Y_VEL
    meteor3.x += METEOR_3_X_VEL
    meteor3.y += METEOR_3_Y_VEL

    if meteor1.x > 999:
        meteor1.x = 1
    if meteor1.x < 1:
        meteor1.x = 999
    if meteor1.y > 499:
        meteor1.y = 1
    if meteor1.y < 1:
        meteor1.y = 499

    if meteor2.x > 999:
        meteor2.x = 1
    if meteor2.x < 1:
        meteor2.x = 999
    if meteor2.y > 499:
        meteor2.y = 1
    if meteor2.y < 1:
        meteor2.y = 499

    if meteor3.x > 999:
        meteor3.x = 1
    if meteor3.x < 1:
        meteor3.x = 999
    if meteor3.y > 499:
        meteor3.y = 1
    if meteor3.y < 1:
        meteor3.y = 499


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, True, WHITE)
    WINDOW.blit(draw_text, (WIDTH/2-draw_text.get_width()/2, HEIGHT/2-draw_text.get_height()/2))
    pg.display.update()
    pg.time.delay(5000)


def handle_bullets(yellow_bullets, red_bullets, yellow, red, meteor1, meteor2, meteor3):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pg.event.post(pg.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
        elif meteor1.colliderect(bullet) or meteor2.colliderect(bullet) or meteor3.colliderect(bullet):
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pg.event.post(pg.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
        elif meteor1.colliderect(bullet) or meteor2.colliderect(bullet) or meteor3.colliderect(bullet):
            red_bullets.remove(bullet)

    if yellow.colliderect(meteor1):
        meteor1.x = 480
        meteor1.y = 240
        pg.event.post(pg.event.Event(YELLOW_HIT))
    if yellow.colliderect(meteor2):
        meteor2.x = 480
        meteor2.y = 240
        pg.event.post(pg.event.Event(YELLOW_HIT))
    if yellow.colliderect(meteor3):
        meteor3.x = 480
        meteor3.y = 240
        pg.event.post(pg.event.Event(YELLOW_HIT))

    if red.colliderect(meteor1):
        meteor1.x = 480
        meteor1.y = 240
        pg.event.post(pg.event.Event(RED_HIT))
    if red.colliderect(meteor2):
        meteor2.x = 480
        meteor2.y = 240
        pg.event.post(pg.event.Event(RED_HIT))
    if red.colliderect(meteor3):
        meteor3.x = 480
        meteor3.y = 240
        pg.event.post(pg.event.Event(RED_HIT))


def main():
    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    red = pg.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pg.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    meteor1 = pg.Rect(480, 240, METEOR_WIDTH, METEOR_HEIGHT)
    meteor2 = pg.Rect(480, 240, METEOR_WIDTH, METEOR_HEIGHT)
    meteor3 = pg.Rect(480, 240, METEOR_WIDTH, METEOR_HEIGHT)

    clock = pg.time.Clock()  # Itt inicializáljuk a clock-ot

    run = True
    while run:
        key_pressed = pg.key.get_pressed()
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if key_pressed[pg.K_LCTRL] and len(yellow_bullets) < MAX_BULLETS:
                bullet = pg.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2, 10, 5)
                yellow_bullets.append(bullet)
                BULLET_FIRE_SOUND.play()
            if key_pressed[pg.K_RCTRL] and len(red_bullets) < MAX_BULLETS:
                bullet = pg.Rect(red.x, red.y + red.height // 2, 10, 5)
                red_bullets.append(bullet)
                BULLET_FIRE_SOUND.play()
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_FIRE_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_FIRE_SOUND.play()

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow wins!"
        if yellow_health <= 0:
            winner_text = "Red wins!"
        if winner_text != "":
            draw_winner(winner_text)
            break

        yellow_control(key_pressed, yellow)
        red_control(key_pressed, red)
        meteor_controller(meteor1, meteor2, meteor3)
        handle_bullets(yellow_bullets, red_bullets, yellow, red, meteor1, meteor2, meteor3)
        draw_window(red, yellow, red_health, yellow_health, red_bullets, yellow_bullets, meteor1, meteor2, meteor3)
    pg.quit()

if __name__ == "__main__":
    main()
