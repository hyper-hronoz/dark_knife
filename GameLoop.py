import pygame, sys

pygame.init()

screen_width = 1200
screen_width = 700

screen = pygame.display.set_mode((screen_width, screen_width))
clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill("black")
	pygame.display.update()
	clock.tick(60)

# venv\Scripts\activate.bat 
# python engine\TestGameLoop.py