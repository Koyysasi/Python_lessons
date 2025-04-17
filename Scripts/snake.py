import random

import pygame as pg

pg.init()

WHITE = (255,255,255)
YELLOW = (255,255,102)
BLACK = (0,0,0)
RED = (210,50,80)
GREEN = (0,255,0)
BLUE = (50,150,210)

WIDTH = 600
HEIGHT = 400

WINDOW = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("siklós")

CLOCK = pg.time.Clock()

SNAKE_BLIKK = 10
SNAKE_SPEED = 15

FONT_STYLE = pg.font.SysFont("Arial", 25)
SCORE_FONT = pg.font.SysFont("Arial", 35)

def your_score(score):
	value = SCORE_FONT.render("Pontszámod: " + str(score), True, YELLOW)
	WINDOW.blit(value, [0,0])


def our_snake(snake_block, snake_list):
	for x in snake_list:
		pg.draw.rect(WINDOW, BLACK, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
	text = FONT_STYLE.render(msg, True, YELLOW)
	WINDOW.blit(text, [WIDTH / 6, HEIGHT / 3])

def main():
	game_over = False
	game_close = False

	x1 = WIDTH / 2
	y1 = HEIGHT / 2

	x1_change = 0
	y1_change = 0

	length_of_snake = 1
	snake_list = []

	foodx = round(random.randrange(0,WIDTH-SNAKE_BLIKK)/10.0)*10.0
	foody = round(random.randrange(0, HEIGHT - SNAKE_BLIKK) / 10.0) * 10.0

	while not game_over:
		while game_close:
			WINDOW.fill(BLUE)
			message("Vesztettél", RED)
			your_score(length_of_snake-1)
			pg.display.update()

			for event in pg.event.get():
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_q:
						game_over = True
						game_close = False
					if event.key == pg.K_r:
						main()
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_a:
					x1_change = -SNAKE_BLIKK
					y1_change = 0
				if event.key == pg.K_d:
					x1_change = SNAKE_BLIKK
					y1_change = 0
				if event.key == pg.K_w:
					x1_change = 0
					y1_change = SNAKE_BLIKK
				if event.key == pg.K_a:
					x1_change = 0
					y1_change = -SNAKE_BLIKK
			if event.type == pg.QUIT:
				game_over = True

		if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
			game_over = True
		x1 += x1_change
		y1 += y1_change
		WINDOW.fill(BLUE)
		pg.draw.rect(WINDOW,GREEN,[foodx,foody,SNAKE_BLIKK,SNAKE_BLIKK])
		snake_head = [x1, y1]
		snake_list.append(snake_head)
		if len(snake_list) > length_of_snake:
			del snake_list[0]

		for x in snake_list[:-1]:
			if x == snake_head:
				game_close = True

		our_snake(SNAKE_BLIKK, snake_list)
		your_score(length_of_snake-1)

		pg.display.update()

		pg.display.update()

		if x1 == foodx and y1 == foody:
			foodx = round(random.randrange(0,WIDTH-SNAKE_BLIKK) / 10) *10
			foody = round(random.randrange(0, HEIGHT - SNAKE_BLIKK) / 10) * 10
			length_of_snake += 1

		CLOCK.tick(SNAKE_SPEED)
	pg.quit()
	quit()

if __name__ == "__main__":
	main()