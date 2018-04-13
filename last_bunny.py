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
grid_width = 10
grid_height = 5
puzzle_grid = Puzzle_grid("Grid #1", grid_width, grid_height, screen, w, h)
puzzle_grid.draw_grid(0.1,0.1)

#for testing
puzzle_grid.show_grid() #draws grid on terminal

#game loop
while (True):

	#check user input
	for event in pygame.event.get():
		#pressing 'x' on the window
		if (event.type == QUIT):
			pygame.quit()
			exit()

		#pressing right click on the mouse
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_posx, mouse_posy = pygame.mouse.get_pos()
			if event.button == 1:

				#check if shapes in grid was clicked
				puzzle_grid.detect_shape_click(mouse_posx, mouse_posy)
	
	pygame.display.update()




