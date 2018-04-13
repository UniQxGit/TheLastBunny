#The grid for puzzle mechanic aspect of the game

#needs: 
import pygame
from pygame.locals import *
import random

#assets
gems_path = "Assets/Gems/" #assuming inside this folder 4 images named like "Gem_x.jpg" where is x -> (1-4)


class Puzzle_grid:
	#logic variables
	name = "undefined"
	grid = [[]] #this will contain values (1->4) to describe shape value (0 would be empty)

	#so we can populate stuff on the screen
	game_screen = None
	screen_w = None
	screen_h = None

	#UI variables
	grid_rect = [[]] #array of rectangles for mouse clicking
	whole_grid_rect = None #rectangle that encapsulates entire grid, for mouse clicking
	percent_w = None 
	percent_h = None
	shape_w = None
	shape_h = None

	#For "animations"
	clicked_a_shape = False
	time_shape_clicked = None
	animation_delay = 300

	def __init__(self, name, grid_size, shape_size, screen, screen_w, screen_h):
		self.name = name

		#UI stuff
		self.game_screen = screen
		self.screen_w = screen_w
		self.screen_h = screen_h
		grid_w = grid_size[0]
		grid_h = grid_size[1]
		self.shape_w = shape_size[0]
		self.shape_h = shape_size[1]

		#Logic stuff: populate it with random (0->3)
		self.grid = [ [ 0 for i in range(grid_w) ] for j in range(grid_h) ]
		self.grid_rect = [ [ 0 for i in range(grid_w) ] for j in range(grid_h) ]
		self.populate_grid()

	def show_grid(self):
		print ("Puzzle Grid: " + self.name)
		for i in range(len(self.grid)):
			for j in range(len(self.grid[0])):
				print (self.grid[i][j], end = " ")
			print("")

	def shape_to_string(self, i, j):
		return "[" + str(i) + "][" + str(j) + "]" + ", value: " + str(self.grid[i][j])


	# populates the grid with random numbers from 0 -> 3 (3 types of shapes)
	def populate_grid(self):
		for i in range(len(self.grid)):
			for j in range(len(self.grid[0])):
				self.grid[i][j] = random.randint(1,4)

	#percent_w, percent_h is the position offsetted from game screen
	def draw_grid(self, percent_w, percent_h):

		#save these for updating the image
		self.percent_w = percent_w
		self.percent_h = percent_h

		#grid size will be determined by the shape size
		shape_w = self.shape_w
		shape_h = self.shape_h
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
		shape_image = pygame.image.load(gems_path + "Gem_" + str(shape_value) + ".jpg")
		shape_image = pygame.transform.scale(shape_image, size)
		return shape_image

	#see if user clicked on grid, and find out which shape was clicked
	def detect_shape_click (self, mouse_posx, mouse_posy):

		#for animation delay
		self.clicked_a_shape = True
		self.time_shape_clicked = pygame.time.get_ticks()

		#check if click was within grid in the first place
		if (self.whole_grid_rect.collidepoint(mouse_posx, mouse_posy)):
			#check which shape was clicked
			for i in range(len(self.grid_rect)):
				for j in range(len(self.grid_rect[0])):
					if (self.grid_rect[i][j].collidepoint(mouse_posx, mouse_posy)):
						self.pop_shapes(j, i)


	#algorithm for popping the shapes around the shape clicked
	#accepts coordinates (row,col) of shape clicked
	#look only vertical and horizontal straight up
	def pop_shapes (self, row, col):
		print ("clicked shape at " + self.shape_to_string(col, row))

		shape_value = self.grid[col][row]
		#we're gonna mark everything we want to pop to 0
		self.grid[col][row] = 0	#pop the actual clicked shape at the very least

		#look up
		keep_going_up = True
		counter = 1
		while (keep_going_up):
			shape_to_check = col - counter
			in_bounds = (shape_to_check >= 0)
			if (in_bounds and shape_value == self.grid[shape_to_check][row]):
				print ("\tsame shape upwards " + self.shape_to_string(shape_to_check, row))
				self.grid[shape_to_check][row] = 0
			else:
				keep_going_up = False
			counter += 1

		#look down
		keep_going_down = True
		counter = 1
		while (keep_going_down):
			shape_to_check = col + counter
			in_bounds = (shape_to_check < len(self.grid_rect))
			if (in_bounds and shape_value == self.grid[shape_to_check][row]):
				print ("\tsame shape downwards " + self.shape_to_string(shape_to_check, row))
				self.grid[shape_to_check][row] = 0
			else:
				keep_going_down = False
			counter += 1

		#look left
		keep_going_left = True
		counter = 1
		while (keep_going_left):
			shape_to_check = row - counter
			in_bounds = (shape_to_check >= 0)
			if (in_bounds and shape_value == self.grid[col][shape_to_check]):
				print ("\tsame shape upwards " + self.shape_to_string(col, shape_to_check))
				self.grid[col][shape_to_check] = 0
			else:
				keep_going_left = False
			counter += 1

		#look right
		keep_going_right = True
		counter = 1
		while (keep_going_right):
			shape_to_check = row + counter
			in_bounds = (shape_to_check < len(self.grid_rect[0]))
			if (in_bounds and shape_value == self.grid[col][shape_to_check]):
				print ("\tsame shape upwards " + self.shape_to_string(col, shape_to_check))
				self.grid[col][shape_to_check] = 0
			else:
				keep_going_right = False
			counter += 1

		print (" ")

	#check entire grid by columns
	#remove 0's, drop everything above it down, generate new shapes at the very top
	def make_shapes_fall(self):
		#check grid from bottom to top then left to right
		#so, we'd start [max_col][0] -> [max_col-1][0] ... [max_col][1] -> [max_col-1][1]
		max_col = len(self.grid_rect)
		max_row = len(self.grid_rect[0])
		for i in range(max_row): #row
			for j in range(max_col):#col

				#start from bottom
				curr_col = max_col-j-1
				
				#did we find a zero? (empty space)
				if (self.grid[curr_col][i] == 0):
					found_zero = True
				else:
					found_zero = False

				#have we reached the edge?
				counter = 0
				if (curr_col - counter == -1):
					reached_the_edge = True
				else:
					reached_the_edge = False

				#if found zero keep going up until we find a non-zero shape value or hit the edge
				while (found_zero and not reached_the_edge):
					counter += 1
					reached_the_edge = curr_col - counter == -1
					found_zero = self.grid[curr_col - counter][i] == 0
					
				#if we found a shape, drop it all the way down
				if (self.grid[curr_col][i] == 0 and not reached_the_edge):
					self.grid[curr_col][i] = self.grid[curr_col - counter][i]
					self.grid[curr_col - counter][i] = 0

		#repopulate 0's with new random shapes
		for i in range(max_col):
			for j in range(max_row):
				if (self.grid[i][j] == 0):
					self.grid[i][j] = random.randint(1,4)


	#returns true after "animation delay" milliseconds has passed after detect_shape_click() was called
	#usage: make shapes fall after certain amount of seconds
	def delay_done(self, time_now):
		if (self.clicked_a_shape and (time_now - self.time_shape_clicked >= self.animation_delay)):
			self.clicked_a_shape = False
			return True
		return False









