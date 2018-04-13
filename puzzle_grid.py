
#needs: 
import pygame
from pygame.locals import *
import random
#import numpy as geek

#constants

#assets
gems_path = "Assets/Gems/" #assuming inside this folder 4 images named like "Gem_x.jpg" where is x -> (1-4)


class Puzzle_grid:
	#logic variables
	name = "undefined"
	grid = [[]] #this will contain values (0->3) to describe shape value

	#so we can populate stuff on the screen
	game_screen = None
	screen_w = None
	screen_h = None

	#UI variables
	grid_rect = [[]] #array of rectangles for mouse clicking
	whole_grid_rect = None #rectangle that encapsulates entire grid, for mouse clicking

	def __init__(self, name, width, height, screen, screen_w, screen_h):
		self.name = name
		self.game_screen = screen
		self.screen_w = screen_w
		self.screen_h = screen_h

		#populate it with random (0->3)
		self.grid = [ [ 0 for i in range(width) ] for j in range(height) ]
		self.grid_rect = [ [ 0 for i in range(width) ] for j in range(height) ]
		self.populate_grid()

	def show_grid(self):
		print ("Puzzle Grid: " + self.name)
		for i in range(len(self.grid)):
			for j in range(len(self.grid[0])):
				print (self.grid[i][j], end = " ")
			print("")


	# populates the grid with random numbers from 0 -> 3 (3 types of shapes)
	def populate_grid(self):
		for i in range(len(self.grid)):
			for j in range(len(self.grid[0])):
				self.grid[i][j] = random.randint(0,3)

	#percent_w, percent_h is the position offsetted from game screen
	def draw_grid(self, percent_w, percent_h):

		#grid size will be determined by the shape size
		shape_w = 20
		shape_h = 20
		print (len(self.grid) * shape_w)
		grid_size = (len(self.grid[0])  * shape_w, len(self.grid)* shape_h)
		grid_pos = (self.screen_w * percent_w, self.screen_h * percent_h)

		#setup collision detection for grid as a whole
		self.whole_grid_rect = pygame.Rect(grid_pos, grid_size)

		#draw the shapes
		for i in range(len(self.grid)):
			for j in range(len(self.grid[0])):
				shape_image = self.draw_shape(shape_w, shape_h, self.grid[i][j])
				shape_pos = (grid_pos[0] + (shape_w*j), grid_pos[1] + (shape_h*i))
				self.game_screen.blit(shape_image, shape_pos)
				self.grid_rect[i][j] = pygame.Rect(shape_pos, (shape_w, shape_h))
		
	#draw a shape (will draw multiple of these to draw grid)
	def draw_shape (self, size_w, size_h, shape_value):
		size = (size_w, size_h)
		shape_image = pygame.image.load(gems_path + "Gem_" + str(shape_value + 1) + ".jpg")
		shape_image = pygame.transform.scale(shape_image, size)
		return shape_image

	#see if user clicked on grid, and find out which shape was clicked
	def detect_shape_click (self, mouse_posx, mouse_posy):

		#check if click was within grid in the first place
		if (self.whole_grid_rect.collidepoint(mouse_posx, mouse_posy)):
			#check which shape was clicked
			for i in range(len(self.grid_rect)):
				for j in range(len(self.grid_rect[0])):
					if (self.grid_rect[i][j].collidepoint(mouse_posx, mouse_posy)):
						print ("clicked shape at (" + str(j) + ", " + str(i) + "), value = " + str(self.grid[i][j]))






