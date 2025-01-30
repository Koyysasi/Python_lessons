import pygame
import os

pygame.init()

WIDTH = 900
HEIGHT = 500

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star Wars")

WHITE = (255, 255, 255)

FPS = 60
VEL = 5
SPACESHIP_WIDTH = 80
SPACESHIP_HEIGHT = 60

# Spaceship képek betöltése
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def yellow_control(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:  # Balra
        yellow.x -= VEL
    if keys_pressed[pygame.K_d]:  # Jobbra
        yellow.x += VEL

    if keys_pressed[pygame.K_w]:  # Fel
        yellow.y -= VEL
    if keys_pressed[pygame.K_s]:  # Le
        yellow.y += VEL

def red_control(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:  # Balra
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT]:  # Jobbra
        red.x += VEL
    if keys_pressed[pygame.K_UP]:  # Fel
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN]:  # Le
        red.y += VEL

def draw_window(red, yellow):
    WINDOW.fill(WHITE)
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_control(keys_pressed, yellow)
        red_control(keys_pressed, red)

        draw_window(red, yellow)

    pygame.quit()

if __name__ == "__main__":
    main()
