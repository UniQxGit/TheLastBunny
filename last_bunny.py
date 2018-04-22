# Last Bunny

# Authors: 
# John Lee - hyunmail94@csu.fullerton.edu
# Andre Victoria - andreappstuff@csu.fullerton.edu

import pygame
from pygame.locals import *
from puzzle_grid import Puzzle_grid #puzzle_grid.py
from character import * #character.py
import math

#pygame setup
pygame.init()
pygame.display.set_caption("The Last Bunny")
bg = pygame.image.load("Assets/InGame/Level_1.png")
screen = pygame.display.set_mode(bg.get_rect().size)
w, h = pygame.display.get_surface().get_size()

#-----LevelAssets-----
#SkillIcons (small)
skill_icon_small_1 = pygame.image.load("Assets/InGame/Skillicon_small_1.png").convert_alpha()
skill_icon_small_2 = pygame.image.load("Assets/InGame/Skillicon_small_2.png").convert_alpha()
skill_icon_small_3 = pygame.image.load("Assets/InGame/Skillicon_small_3.png").convert_alpha()
skill_icon_small_4 = pygame.image.load("Assets/InGame/Skillicon_small_4.png").convert_alpha()

battle_menu = pygame.image.load("Assets/InGame/battle_menu.png").convert_alpha();

#status bars
status_player = pygame.image.load("Assets/InGame/status_bunny.png").convert_alpha()
status_enemy_skel = pygame.image.load("Assets/InGame/enemy_status_skel.png").convert_alpha()

#fonts
bit_8_font = pygame.font.Font("Assets/Fonts/8_bit_pusab.ttf", 13)
bit_8_font_status = pygame.font.Font("Assets/Fonts/8_bit_pusab.ttf", 7)
double_bubble_font = pygame.font.Font("Assets/Fonts/Double_Bubble_shadow.otf", 25)

#-----game setup-----
#create grid
grid_size = (8, 9)
shape_size = (63, 65)
puzzle_grid = Puzzle_grid("Grid #1", grid_size, shape_size, screen, w, h)
puzzle_grid.draw_grid(710, 133) 

#create character (bunny)
main_bunny = Character(screen, "The last bunny", puzzle_grid, 100)
#create dummy enemy
enemy_1 = Character(screen, "skeleton_1", None, 50)
enemy_2 = Character(screen, "skeleton_2", None, 50)
enemy_3 = Character(screen, "skeleton_3", None, 50)

#update UI, this will be called at the end part of the game loop
def update_UI():
	#update status bar UI for all characters
	global main_bunny
	global enemy_1
	main_bunny.status_bar_UI(status_player, (350,7), bit_8_font, (460, 50))
	enemy_1.status_bar_UI(status_enemy_skel, (0, 480), bit_8_font_status, (75, 520))
	enemy_2.status_bar_UI(status_enemy_skel, (0, 560), bit_8_font_status, (75, 600))
	enemy_3.status_bar_UI(status_enemy_skel, (0, 640), bit_8_font_status, (75, 680))

	#update the grid
	global puzzle_grid
	puzzle_grid.draw_grid(710,133)

#turn taking
turn_rotation = [main_bunny, enemy_1, enemy_2, enemy_3]
character_num = 4
rotation_counter = 4
active_character = turn_rotation[rotation_counter % character_num]

#game loop
while (True):
	#Draw UI
	
	#if Level 1
	screen.blit(bg ,(0,0)) #redraw background

	#BattleMenu Assets
	screen.blit(battle_menu , (280,550))

	screen.blit(skill_icon_small_1 ,(315,560))
	skill_text = bit_8_font.render("AVOID", False, (255, 255, 255))
	screen.blit(skill_text,(360, 575))

	screen.blit(skill_icon_small_2 ,(315,560+37*1))
	skill_text = bit_8_font.render("BE CUTE", False, (255, 255, 255))
	screen.blit(skill_text,(360, 575+37*1))

	screen.blit(skill_icon_small_3 ,(315,560+37*2))
	skill_text = bit_8_font.render("SCRATCH", False, (255, 255, 255))
	screen.blit(skill_text,(360, 575+37*2))

	screen.blit(skill_icon_small_4 ,(315,560+37*3))
	skill_text = bit_8_font.render("RAGE!!!", False, (255, 255, 255))
	screen.blit(skill_text,(360, 575+37*3))


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

				#check if a shape the in grid was clicked and pop em if it was
				if (active_character == main_bunny):
					puzzle_grid.detect_shape_click(mouse_posx, mouse_posy)

					#TESTING ATTACK (remove this later)
					main_bunny.attack(enemy_1, skill_1)
					rotation_counter += 1
					active_character = turn_rotation[rotation_counter % character_num]

	#AI moves
	if (active_character != main_bunny):
		#attack if still alive
		if (active_character.health > 0):
			active_character.attack(main_bunny, AI_skill_1) 

		#next person's turn
		rotation_counter += 1
		active_character = turn_rotation[rotation_counter % character_num]

	#delay after a shape click
	if (puzzle_grid.delay_done(now)):
		puzzle_grid.make_shapes_fall()

	#delay for shapes falling
	if (puzzle_grid.falling_done(now)):
		puzzle_grid.make_shapes_fall()
	
	#update screen
	update_UI()

	pygame.display.update()




