#Rabids Uno

# Authors: 
# John Lee - hyunmail94@csu.fullerton.edu
# Andre Victoria - andreappstuff@csu.fullerton.edu

import pygame
from pygame.locals import *
from puzzle_grid import Puzzle_grid 


#display array
def display_arr(arr = []):
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			print (arr[i][j], end = " ")
		print ("")

#setup
pygame.init()
pygame.display.set_caption("The Last Bunny")
image = pygame.image.load("background.png")
screen = pygame.display.set_mode(image.get_rect().size)
w, h = pygame.display.get_surface().get_size()

#create grid
grid_size = (10, 5)
shape_size = (20, 20)
puzzle_grid = Puzzle_grid("Grid #1", grid_size, shape_size, screen, w, h)
puzzle_grid.draw_grid(0.1, 0.1) 

#for testing
puzzle_grid.show_grid() #draws grid on terminal

#game loop
while (True):

	#time right now (used for delaying stuff)
	now = pygame.time.get_ticks()

	#check user input
	for event in pygame.event.get():
		#pressing 'x' on the window
		if (event.type == QUIT):
			pygame.quit()
			exit()

		#mouse was clicked
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_posx, mouse_posy = pygame.mouse.get_pos()

			#pressing left click on the mouse
			if event.button == 1:

				#check if shapes in grid was clicked
				puzzle_grid.detect_shape_click(mouse_posx, mouse_posy)
				puzzle_grid.draw_grid(0.1,0.1)

	#delaying "animations" for grid
	if (puzzle_grid.delay_done(now)):
		puzzle_grid.make_shapes_fall()
		puzzle_grid.draw_grid(0.1,0.1)
	
	pygame.display.update()




