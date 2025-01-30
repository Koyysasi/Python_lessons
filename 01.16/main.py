
import pygame
import os
pygame.mixer.init()
pygame.font.init()
from pygame.examples.setmodescale import clock
import math
import random
from main import handle_bullets

pygame.init()

WIDTH = 900
HEIGHT = 500

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Star Wars")







# Variables
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space.png")), (WIDTH, HEIGHT))

BORDER = pygame.Rect(WIDTH // 2-5, 0, 10, HEIGHT)


BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'explosion.wav'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'laser.wav'))

HEALTH_FONT = pygame.font.SysFont('Arial', 40)
WINNER_FONT = pygame.font.SysFont('Arial', 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3

SPACESHIP_WIDTH = 80
SPACESHIP_HEIGHT = 60

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)

METEOR_WIDTH, METEOR_HEIGHT = 50, 50
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

METEOR_IMAGE = pygame.image.load(os.path.join("Assets", "meteor.png"))
METEOR_1 = pygame.transform.rotate(pygame.transform.scale(METEOR_IMAGE, (METEOR_WIDTH, METEOR_HEIGHT)), 90)
METEOR_2 = pygame.transform.rotate(pygame.transform.scale(METEOR_IMAGE, (METEOR_WIDTH, METEOR_HEIGHT)), 90)
METEOR_3 = pygame.transform.rotate(pygame.transform.scale(METEOR_IMAGE, (METEOR_WIDTH, METEOR_HEIGHT)), 90)


# end variables



def darw_winner(text):
    draw_text = WINNER_FONT.render(text, TRUE,WHITE)
    WINDOW.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
pygame.display.update()
pygame.time.delay(5000)



# Control

def yellow_control(keys_pressed , yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > -15:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width -15 < BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > -10:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height -10 < HEIGHT:
        yellow.y += VEL

def red_control(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL + 15 > BORDER.x:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width -15 < WIDTH:
        red.x += VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height -10 < HEIGHT:
        red.y += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > -10:
        red.y -= VEL

# end control

def drawWindow(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, meteor_1, meteor_2, meteor_3 ):
    WINDOW.blit(SPACE, (0, 0))
    pygame.draw.rect(WINDOW, BLACK, BORDER)



    RED_HEALTH_TEXT = HEALTH_FONT.render(f"Élet: {str(red_health)}")
    YELLOW_HEALTH_TEXT = HEALTH_FONT.render(f"Élet: {str(yellow_health)}")

    WINDOW.blit(RED_HEALTH_TEXT, (WIDTH - RED_HEALTH_TEXT.get_width() -10, 10))
    WINDOW.blit(YELLOW_HEALTH_TEXT, (10, 10))

    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))

    WINDOW.blit(METEOR_1, (meteor_1.x,meteor_1.y))
    WINDOW.blit(METEOR_2, (meteor_2.x,meteor_3.y))
    WINDOW.blit(METEOR_3, (meteor_3.x,meteor_3.y))
    for bullet in red_bullets:
        pygame.draw.rect(WIDTH, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIDTH, YELLOW, bullet)
    pygame.display.update()

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x < 0:
            yellow_bullets.remove(bullet)
    

def meteor_controller(meteor_1, meteor_2, meteor_3):
    meteor_1.x += METEOR_1_X_VEL
    meteor_1.y += METEOR_1_Y_VEL
    meteor_2.x += METEOR_2_X_VEL
    meteor_2.y += METEOR_2_Y_VEL
    meteor_3.x += METEOR_3_X_VEL
    meteor_3.y += METEOR_3_Y_VEL
    
    if meteor_1.x > 999:
        meteor_1.x = 1
    if meteor_1.x < 1:
        meteor_1.x = 999
    if meteor_1.y > 499:
        meteor_1.x = 1
    if meteor_1.y < 1:
        meteor_1.y = 499
    
    if meteor_2.x > 999:
        meteor_2.x = 1
    if meteor_2.x < 1:
        meteor_2.x = 999
    if meteor_2.y > 499:
        meteor_2.x = 1
    if meteor_2.y < 1:
        meteor_2.y = 499

    if meteor_3.x > 999:
        meteor_3.x = 1
    if meteor_3.x < 1:
        meteor_3.x = 999
    if meteor_3.y > 499:
        meteor_3.x = 1
    if meteor_3.y < 1:
        meteor_3.y = 499


def main():
    red = pygame.Rect(700,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    meteor_1 = pygame.Rect(480, 240, METEOR_WIDTH, METEOR_HEIGHT)
    meteor_2 = pygame.Rect(480, 240, METEOR_WIDTH, METEOR_HEIGHT)
    meteor_3 = pygame.Rect(480, 240, METEOR_WIDTH, METEOR_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 20


    # játék futása
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2, 10, 5)
                yellow_bullets.append(bullet)
                BULLET_FIRE_SOUND.play()
            if event.type == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                bullet = pygame.Rect(red.x, red.y + red.height // 2, 10, 5)
                red_bullets.append(bullet)
                BULLET_FIRE_SOUND.play()
        winner_text = ""

        if red_health <= 0:
            winner_text = "Sárga a győztes"
        if yellow_health <= 0:
            winner_text = "Piros a győztes"
        if winner_text != "":
            darw_winner(winner_text)
            break
        key_pressed = pygame.key.get_pressed()
        yellow_control(key_pressed, yellow)
        red_control(key_pressed, red)
        meteor_controller(meteor_1, meteor_2, meteor_3)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        drawWindow(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, meteor_1, meteor_2, meteor_3)
    pygame.quit()

    
    


if __name__ == "__main__":
    main()

