import pygame as pg
import os
import math
import random

pg.mixer.init()
pg.font.init()

pg.init()

WIDTH = 900
HEIGHT = 500

WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Star wars")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

BACKGROUND = pg.transform.scale(pg.image.load(os.path.join('Assets', 'space.png')))

BULLET_HIT_SOUND = pg.mixer.Sound(os.path.join('Assets', 'explosion.wav'))
BULLET_FIRE_SOUND = pg.mixer.Sound(os.path.join('Assets', 'laser.wav'))

HEALTH_FONT = pg.font.SysFont('algerian', 40)
WINNER_FONT = pg.font.SysFont('wingdings', 100)

FPS = 60
VELOCITY = 5
BULLET_VEL = 7
MAX_BULLETS = 3

SPACESHIP_WIDTH = 80
SPACESHIP_HEIGHT = 60


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



def draw_window(red, yellow):
    WINDOW.blit(BACKGROUND, (0,0))

    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    pg.draw.rect(WINDOW, BLACK, BORDER)

    pg.display.update()



def main():

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    red = pg.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pg.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pg.time.Clock()  # Itt inicializáljuk a clock-ot

    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                bullet = pg.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2, 10, 5)
                yellow_bullets.append(bullet)
                BULLET_FIRE_SOUND.play()
        key_pressed = pg.key.get_pressed()
        yellow_control(key_pressed, yellow)
        red_control(key_pressed, red)
        draw_window(red, yellow)
    pg.quit()


if __name__ == "__main__":
    main()
