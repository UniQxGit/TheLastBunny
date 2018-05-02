#The grid for puzzle mechanic aspect of the game

#needs: 
import pygame
from pygame.locals import *
import random

#assets:
gem_image = [None,None,None,None,None] 

#for skill icons (large)
double_bubble_font = None
skill_icon_large_1 = None
skill_icon_large_2 = None
skill_icon_large_3 = None
skill_icon_large_4 = None

class Puzzle_grid:
	#logic variables
	name = "undefined"
	grid = [[]] #this will contain values (1->4) to describe shape value (0 would be empty)
	disable_grid = False

	#so we can populate stuff on the screen
	game_screen = None
	screen_w = None
	screen_h = None

	#Stuff we want to communicate to Character using this grid (character.py)
	collected_shapes = [0,0,0,0]
	move_picked = False
	finished_grid_move = False

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
	click_delay = 200

	#for make_shapes_fall_2() "animations"
	shapes_still_falling = True
	time_a_shape_fell = None
	fall_delay = 30

	def __init__(self, name, grid_size, shape_size, screen, screen_w, screen_h):
		self.name = name

		#UI stuff
		self.load_assets()
		self.game_screen = screen
		self.screen_w = screen_w
		self.screen_h = screen_h
		grid_w = grid_size[0]
		grid_h = grid_size[1]
		self.shape_w = shape_size[0]
		self.shape_h = shape_size[1]
		self.collected_shapes = [0,0,0,0]
		self.grid_rect = [ [ 0 for i in range(grid_w) ] for j in range(grid_h) ]

		#Logic stuff: populate it with random (0->3)
		self.grid = [ [ 0 for i in range(grid_w) ] for j in range(grid_h) ]
		self.populate_grid()

	def load_assets(self):
		global double_bubble_font
		global skill_icon_large_1, skill_icon_large_2, skill_icon_large_3, skill_icon_large_4
		global gem_image

		#for skill icons
		double_bubble_font = pygame.font.Font("Assets/Fonts/Double_Bubble_shadow.otf", 25)
		skill_icon_large_1 = pygame.image.load("Assets/InGame/SkillIcon_1.png").convert_alpha()
		skill_icon_large_2 = pygame.image.load("Assets/InGame/SkillIcon_2.png").convert_alpha()
		skill_icon_large_3 = pygame.image.load("Assets/InGame/SkillIcon_3.png").convert_alpha()
		skill_icon_large_4 = pygame.image.load("Assets/InGame/SkillIcon_4.png").convert_alpha()

		#for gem(aka shapes) images
		gem_image[0] = pygame.image.load("Assets/Gems/Gem_0.png").convert_alpha()
		gem_image[1] = pygame.image.load("Assets/Gems/Gem_1.png").convert_alpha()
		gem_image[2] = pygame.image.load("Assets/Gems/Gem_2.png").convert_alpha()
		gem_image[3] = pygame.image.load("Assets/Gems/Gem_3.png").convert_alpha()
		gem_image[4] = pygame.image.load("Assets/Gems/Gem_4.png").convert_alpha()

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
	def draw_grid(self, x, y):

		#save these for updating the image
		self.percent_w = x
		self.percent_h = y

		#grid size will be determined by the shape size
		shape_w = self.shape_w
		shape_h = self.shape_h
		grid_size = (len(self.grid[0])  * shape_w, len(self.grid)* shape_h)
		grid_pos = (x, y)

		#setup collision detection for grid as a whole
		self.whole_grid_rect = pygame.Rect(grid_pos, grid_size)

		#draw shape count at the top
		self.game_screen.blit(skill_icon_large_1 ,(690,19))
		skill_text = double_bubble_font.render(str(self.collected_shapes[0]), False, (255, 255, 255))
		self.game_screen.blit(skill_text,(770, 100))

		self.game_screen.blit(skill_icon_large_2 ,(790+50*1,19))
		skill_text = double_bubble_font.render(str(self.collected_shapes[1]), False, (255, 255, 255))
		self.game_screen.blit(skill_text,(870+50*1, 100))

		self.game_screen.blit(skill_icon_large_3 ,(890+50*2,19))
		skill_text = double_bubble_font.render(str(self.collected_shapes[2]), False, (255, 255, 255))
		self.game_screen.blit(skill_text,(970+50*2, 100))

		self.game_screen.blit(skill_icon_large_4 ,(990+50*3,19))
		skill_text = double_bubble_font.render(str(self.collected_shapes[3]), False, (255, 255, 255))
		self.game_screen.blit(skill_text,(1070+50*3, 100))

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
		shape_image = pygame.transform.scale(gem_image[shape_value], size)
		return shape_image

	#see if user clicked on grid, and find out which shape was clicked
	def detect_shape_click (self, mouse_posx, mouse_posy):

		#prevent multiple clicks
		if (self.disable_grid == False):
			#check if click was within grid in the first place
			if (self.whole_grid_rect.collidepoint(mouse_posx, mouse_posy)):
				self.disable_grid = True
				#check which shape was clicked
				for i in range(len(self.grid_rect)):
					for j in range(len(self.grid_rect[0])):
						if (self.grid_rect[i][j].collidepoint(mouse_posx, mouse_posy)):
							#for animation delay
							self.clicked_a_shape = True
							self.time_shape_clicked = pygame.time.get_ticks()
							#pop em
							self.pop_shapes(j, i)


	#algorithm for popping the shapes around the shape clicked
	#accepts coordinates (row,col) of shape clicked
	#look only vertical and horizontal straight up and then recursively do it the matched shapes
	def pop_shapes (self, row, col):
		print ("clicked shape at " + self.shape_to_string(col, row))

		shape_value = self.grid[col][row]
		#we're gonna mark everything we want to pop to 0
		self.grid[col][row] = 0	#pop the actual clicked shape at the very least
		self.collected_shapes[shape_value-1] += 1

		#look up
		keep_going_up = True
		counter = 1
		while (keep_going_up):
			shape_to_check = col - counter
			in_bounds = (shape_to_check >= 0)
			if (in_bounds and shape_value == self.grid[shape_to_check][row]):
				self.pop_shapes(row, shape_to_check) #recursive!
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
				self.pop_shapes(row, shape_to_check) #recursive!
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
				self.pop_shapes(shape_to_check, col) #recursive!
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
				self.pop_shapes(shape_to_check, col) #recursive!
				self.grid[col][shape_to_check] = 0
			else:
				keep_going_right = False
			counter += 1

	#find the zero's(empty spaces) and replace them with the shape above it
	#if at the very top and we find a zero, generate a random shape
	#usage: run this until no more empty spaces in grid
	#this version is intended to make the falling animation more apparent (a little more costly)
	def make_shapes_fall(self):

		max_col = len(self.grid_rect)
		max_row = len(self.grid_rect[0])

		#assume no zero found
		zero_was_found = False
		for i in range(max_col): #row
			for j in range(max_row): #col

				#start from the bottom
				curr_col = max_col-i-1

				#did we find a zero? (empty space)
				if (self.grid[curr_col][j] == 0):
					zero_was_found = True
					found_zero = True
				else:
					found_zero = False

				#have we reached the edge?
				counter = 0
				if (curr_col == 0):
					reached_the_edge = True
				else:
					reached_the_edge = False

				#if found zero, make shape above it fall
				if (found_zero and not reached_the_edge):
					shape_above = self.grid[curr_col - 1][j]
					self.grid[curr_col][j] = shape_above
					self.grid[curr_col - 1][j] = 0
				#if found zero and we're at the top, generate a random shape
				elif (found_zero and reached_the_edge):
					random_shape = random.randint(1,4)
					self.grid[curr_col][j] = random_shape

		#falling delay
		self.time_a_shape_fell = pygame.time.get_ticks()
		if (zero_was_found):
			self.shapes_still_falling = True
		else:
			self.shapes_still_falling = False
			if (self.move_picked):
				self.move_picked = False
				self.finished_grid_move = True
				print("finished grid move, now pick a skill\n")

	#returns true after "animation delay" milliseconds has passed after detect_shape_click() was called
	#usage: make shapes fall after certain amount of seconds
	def delay_done(self, time_now):
		if (self.clicked_a_shape and (time_now - self.time_shape_clicked >= self.click_delay)):
			self.move_picked = True
			self.clicked_a_shape = False
			return True
		return False


	def one_space_fall_done(self, time_now):
		if (self.time_a_shape_fell == None):
			return True

		if (self.shapes_still_falling and (time_now - self.time_a_shape_fell >= self.fall_delay)):
			return True
		return False





