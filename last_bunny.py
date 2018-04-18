# Last Bunny

# Authors: 
# John Lee - hyunmail94@csu.fullerton.edu
# Andre Victoria - andreappstuff@csu.fullerton.edu

import pygame
from pygame.locals import *
from puzzle_grid import Puzzle_grid 
import math

#setup
pygame.init()
pygame.display.set_caption("The Last Bunny")
bg = pygame.image.load("Assets/InGame/Level_1.png")
screen = pygame.display.set_mode(bg.get_rect().size)
w, h = pygame.display.get_surface().get_size()

#create grid
grid_size = (8, 9)
shape_size = (63, 65)
puzzle_grid = Puzzle_grid("Grid #1", grid_size, shape_size, screen, w, h)
puzzle_grid.draw_grid(0.7, 0.1) 

#for testing
puzzle_grid.show_grid() #draws grid on terminal

#LevelAssets

#SkillIcons (Large)
skill_icon_large_1 = pygame.image.load("Assets/InGame/SkillIcon_1.png").convert_alpha()
skill_icon_large_2 = pygame.image.load("Assets/InGame/SkillIcon_2.png").convert_alpha()
skill_icon_large_3 = pygame.image.load("Assets/InGame/SkillIcon_3.png").convert_alpha()
skill_icon_large_4 = pygame.image.load("Assets/InGame/SkillIcon_4.png").convert_alpha()

#SkillIcons (Large)
skill_icon_small_1 = pygame.image.load("Assets/InGame/Skillicon_small_1.png").convert_alpha()
skill_icon_small_2 = pygame.image.load("Assets/InGame/Skillicon_small_2.png").convert_alpha()
skill_icon_small_3 = pygame.image.load("Assets/InGame/Skillicon_small_3.png").convert_alpha()
skill_icon_small_4 = pygame.image.load("Assets/InGame/Skillicon_small_4.png").convert_alpha()

battle_menu = pygame.image.load("Assets/InGame/battle_menu.png").convert_alpha();

bit_8_font = pygame.font.Font("Assets/Fonts/8_bit_pusab.ttf", 13)
double_bubble_font = pygame.font.Font("Assets/Fonts/Double_Bubble_shadow.otf", 25)



#game loop
while (True):
	#Draw UI
	
	#if Level 1
	screen.blit(bg ,(0,0))
	
	screen.blit(skill_icon_large_1 ,(690,19))
	skill_text = double_bubble_font.render(str(puzzle_grid.collected_shapes[0]), False, (255, 255, 255))
	screen.blit(skill_text,(770, 100))

	screen.blit(skill_icon_large_2 ,(790+50*1,19))
	skill_text = double_bubble_font.render(str(puzzle_grid.collected_shapes[1]), False, (255, 255, 255))
	screen.blit(skill_text,(870+50*1, 100))

	screen.blit(skill_icon_large_3 ,(890+50*2,19))
	skill_text = double_bubble_font.render(str(puzzle_grid.collected_shapes[2]), False, (255, 255, 255))
	screen.blit(skill_text,(970+50*2, 100))

	screen.blit(skill_icon_large_4 ,(990+50*3,19))
	skill_text = double_bubble_font.render(str(puzzle_grid.collected_shapes[3]), False, (255, 255, 255))
	screen.blit(skill_text,(1070+50*3, 100))


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


	puzzle_grid.draw_grid(710, 133) 	


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
				puzzle_grid.detect_shape_click(mouse_posx, mouse_posy)
				puzzle_grid.draw_grid(710,133)

	#delaying "animations" for grid
	if (puzzle_grid.delay_done(now)):
		puzzle_grid.make_shapes_fall()
		puzzle_grid.draw_grid(710,133)
	
	pygame.display.update()




