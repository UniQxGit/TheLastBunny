# Last Bunny

# Authors: 
# John Lee - hyunmail94@csu.fullerton.edu
# Andre Victoria - andreappstuff@csu.fullerton.edu

import pygame
from pygame.locals import *
from puzzle_grid import Puzzle_grid #puzzle_grid.py
from character import Character #character.py
from skills import * #has the skill definitions, ex. skill_1
from sprites import *
import math
import time

#pygame setup
pygame.init()
pygame.display.set_caption("The Last Bunny")
bg = [
	pygame.image.load("Assets/opening.png"),
	pygame.image.load("Assets/InGame/Level_1.png"),
	pygame.image.load("Assets/InGame/Level_1.png")
]


screen = pygame.display.set_mode(bg[0].get_rect().size)#,pygame.FULLSCREEN
w, h = pygame.display.get_surface().get_size()

#-----LevelAssets-----

#music
music = ["Assets/Music/opening.mp3","Assets/Music/cutscene.mp3","Assets/Music/battle.mp3"]
pygame.mixer.music.load(music[0])
pygame.mixer.music.play(-1)

#status bars
status_player = pygame.image.load("Assets/InGame/status_bunny.png").convert_alpha()
status_enemy_skel = pygame.image.load("Assets/InGame/enemy_status_skel.png").convert_alpha()

#fonts
bit_8_font = pygame.font.Font("Assets/Fonts/8_bit_pusab.ttf", 13)
bit_8_font_status = pygame.font.Font("Assets/Fonts/8_bit_pusab.ttf", 7)
double_bubble_font = pygame.font.Font("Assets/Fonts/Double_Bubble_shadow.otf", 25)

#Load level
level = pygame.image.load("Assets/InGame/Levels_01.png").convert_alpha();

#Load Animations
#bunny
bunny_animation = Animation("bunny","idle",2)
bunny_animation.add_anim("attack",12)
bunny_animation.add_anim("attacked",4)
bunny_animation.add_anim("die",4)

#skeleton
skeleton_animation = Animation("skel","idle",11)
skeleton_animation.add_anim("attack",18)
skeleton_animation.add_anim("attacked",8)
skeleton_animation.add_anim("die",15)

#opening skels
opening_skel_animation = Animation("opening_skel","show",5)
opening_bclouds_animation = Animation("clouds_black","show",5)


#load Sprites
bunny = Sprite.animation(bunny_animation,"Bunny")
skeleton1 = Sprite.animation(skeleton_animation,"Skeleton1")
skeleton2 = Sprite.animation(skeleton_animation,"Skeleton2")
skeleton3 = Sprite.animation(skeleton_animation,"Skeleton3")
skeleton4 = Sprite.animation(skeleton_animation,"Skeleton4")
skeleton5 = Sprite.animation(skeleton_animation,"Skeleton5")
skeleton6 = Sprite.animation(skeleton_animation,"Skeleton6")
opening_skel = Sprite.animation(opening_skel_animation,"openingSkeleton")
opening_bclouds = Sprite.animation(opening_bclouds_animation,"blackClouds")
play_button = Sprite.image(pygame.image.load("Assets/Opening/play_button.png").convert_alpha(),"play")
quit_button = Sprite.image(pygame.image.load("Assets/Opening/quit_button.png").convert_alpha(),"quit")


#Test. To Make sure functions are called just once in the loop.
called1 = False
called2 = False

#Test. blank white status bar for targeted character
targeted_status_img = pygame.image.load("Assets/InGame/enemy_status_over.png").convert_alpha()

#-----game setup-----
#create grid
grid_size = (8, 9)
shape_size = (63, 65)
puzzle_grid = Puzzle_grid("Grid #1", grid_size, shape_size, screen, w, h)
puzzle_grid.draw_grid(710, 133) 
screen.fill((0,0,0))
pygame.display.update()

#create character (bunny)
main_bunny = Character(screen, "The last bunny", puzzle_grid, 100, bunny, (415,230))
#create dummy enemy
enemy_1 = Character(screen, "skeleton_1", None, 50, skeleton1, (180,370))
enemy_2 = Character(screen, "skeleton_2", None, 50, skeleton2, (220,370))
enemy_3 = Character(screen, "skeleton_3", None, 50, skeleton3, (240,370))
#setup specific UI
main_bunny.setup_status_bar_UI(status_player, (350,7), bit_8_font, (460, 50), targeted_status_img)
enemy_1.setup_status_bar_UI(status_enemy_skel, (0, 480), bit_8_font_status, (75, 520), targeted_status_img)
enemy_2.setup_status_bar_UI(status_enemy_skel, (0, 560), bit_8_font_status, (75, 600), targeted_status_img)
enemy_3.setup_status_bar_UI(status_enemy_skel, (0, 640), bit_8_font_status, (75, 680), targeted_status_img)


#Level Data
which_scene = 0;
	#0 : Opening
	#1 : Cutscene
	#2 : Level 1
	#3 : Level 2
can_splash = True; #play splash screen only once.

#splash_screen.image.set_alpha(0)
pygame.time.delay(2000)

#splash_screen.draw(screen,(0,0))


#show splash screen
splash_screen = Sprite.image(pygame.image.load("Assets/splash_screen.png").convert(),"splash")
splash_screen.fade_in(screen,5.0)
can_splash = False
splash_screen.fade_out(screen,2.0)

#opening Animation
opening_bright = Sprite.image(pygame.image.load("Assets/bright_sky.png").convert(),"bright")
opening_dark = Sprite.image(pygame.image.load("Assets/dark_sky.png").convert(),"dark")
opening = Sprite.image(pygame.image.load("Assets/opening.png").convert(),"opening")
intro_bunny = Sprite.image(pygame.image.load("Assets/Opening/Bunny.png").convert_alpha(),"intro_bunny")

end = pygame.time.get_ticks() + 3000 
while pygame.time.get_ticks() < end:
	for event in pygame.event.get():
		#pressing 'x' on the window
		if (event.type == QUIT):
			pygame.quit()
			exit()
	opening_bright.draw(screen,(0,0))
	pygame.display.update()

#pygame.time.delay(5000)


opening_bclouds.return_to_default = False
opening_skel.return_to_default = False
opening_bclouds.play("show",1)
while opening_bclouds.is_playing:
	for event in pygame.event.get():
			#pressing 'x' on the window
			if (event.type == QUIT):
				pygame.quit()
				exit()
	opening_bclouds.draw(screen,(0,0))
	intro_bunny.draw(screen,(0,0))
	pygame.display.update()
	pygame.time.delay(1)

opening_dark.fade_in(screen,2.0)

opening_skel.play("show",1)
while opening_skel.is_playing:
	for event in pygame.event.get():
			#pressing 'x' on the window
			if (event.type == QUIT):
				pygame.quit()
				exit()
	opening_dark.draw(screen,(0,0))
	opening_skel.draw(screen,(0,0))
	opening_bclouds.draw(screen,(0,0))
	intro_bunny.draw(screen,(0,0))
	pygame.display.update()
	pygame.time.delay(1)

opening_skel.draw(screen,(0,0))
opening_bclouds.draw(screen,(0,0))

pygame.time.delay(3000)


opening.fade_in(screen,5.0)


#update the screen with the new changes, this will be called at the end part of the game loop
def update_screen():
	global can_splash
	if which_scene == 0:
		play_button.draw(screen,(450,315))
		quit_button.draw(screen,(450,460))
	if which_scene == 2:
		#update status bar UI for all characters
		global main_bunny
		global enemy_1
		global level 
		#Level
		screen.blit(level,(133,180))

		main_bunny.draw_status_bar()
		enemy_1.draw_status_bar()
		enemy_2.draw_status_bar()
		enemy_3.draw_status_bar()

		#update the grid
		global puzzle_grid
		puzzle_grid.draw_grid(710,133)

		#update the sprites
		main_bunny.draw_character()
		enemy_1.draw_character()
		enemy_2.draw_character()
		enemy_3.draw_character()

		#update the skill battle menu
		main_bunny.draw_skill_list()


#turn taking
turn_rotation = [main_bunny, enemy_1, enemy_2, enemy_3]
character_num = 4
rotation_counter = 4
active_character = turn_rotation[rotation_counter % character_num] #this will go from 0 -> 4
someone_is_attacking = False
if (turn_rotation[0] == main_bunny):
	can_click_grid = True
else:
	can_click_grid = False

#target picking
skill_picked = None
targeted_character = None
def pick_target (mouse_posx, mouse_posy):
	global turn_rotation, targeted_character
	found_target = False

	for character in turn_rotation:
		if (character.status_bar_rect.collidepoint(mouse_posx, mouse_posy)):
			character.targeted = True
			targeted_character = character
			found_target = True
		else:
			character.targeted = False

	if (found_target == False):
		targeted_character = None


# #game loop
while (True):
	start = time.time()
	#Draw UI
	
	#if Level 1
	screen.blit(bg[which_scene] ,(0,0)) #redraw background

	#BattleMenu Assets

	

	#draw bunny at (395,240)
	#bunny.draw(screen,(415,230))
	#skeleton1.draw(screen,(180,370))
	#skeleton2.draw(screen,(220,370))
	#skeleton3.draw(screen,(240,370))
	#skeleton4.draw(screen,(180,390))
	#skeleton5.draw(screen,(220,390))
	#skeleton6.draw(screen,(240,390))

	#time right now (used for delaying stuff)
	now = pygame.time.get_ticks()

	# #Test animation play calls
	# if now > 5000 and called1 == False:
	# 	#skeleton1.play("attack",3)
	# 	#bunny.play("attack",3)
	# 	called1 = True

	# if now > 10000 and called2 == False and skeleton2.is_playing == False:
	# 	skeleton2.return_to_default = False
	# 	#skeleton2.play("die",1)
	# 	#skeleton6.play("attack",3)
	# 	called2 = True

	#check user input
	for event in pygame.event.get():
		#pressing 'x' on the window
		if (event.type == QUIT):
			pygame.quit()
			exit()

		#mouse was clicked
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_posx, mouse_posy = pygame.mouse.get_pos()

			#possible improvement: can make this cleaner by checking detection first for skill picking
			#check if it's our turn and no one is currently doing an attack animation
			if (event.button == 1):
				if (play_button.rect.collidepoint(mouse_posx, mouse_posy)):
					which_scene = 2
					pygame.mixer.music.load(music[2])
					pygame.mixer.music.play(-1)
				elif (quit_button.rect.collidepoint(mouse_posx, mouse_posy)):
					pygame.quit()
					exit()
				if (active_character == main_bunny and someone_is_attacking == False and which_scene > 1):
					#step 1: click on grid
					if main_bunny.puzzle_grid.finished_grid_move == False:
						puzzle_grid.detect_shape_click(mouse_posx, mouse_posy)

					#step 3: click skill
					if targeted_character != None:
						skill_picked = main_bunny.detect_skill_click(targeted_character, mouse_posx, mouse_posy)

						#start attack
						if (skill_picked != None):
							main_bunny.start_attack(targeted_character, skill_picked)

							#reset values
							someone_is_attacking = True
							skill_picked = None
							main_bunny.puzzle_grid.finished_grid_move = False
							main_bunny.puzzle_grid.disable_grid = False
							#clear targeting
							targeted_character.targeted = False
							targeted_character = None

					#step 2: click target
					if main_bunny.puzzle_grid.finished_grid_move == True and skill_picked == None:
						pick_target(mouse_posx, mouse_posy)

	if which_scene > 1:
		#AI moves
		if (active_character != main_bunny and someone_is_attacking == False):
			if (active_character.health > 0):
				#attack if still alive
				#active_character.show_info()
				active_character.start_attack(main_bunny, AI_skill_1) 
				someone_is_attacking = True
			else:
				#skip em if they're dead
				rotation_counter += 1
				active_character = turn_rotation[rotation_counter % character_num]
					

		#delay finished after a shape click
		if (puzzle_grid.delay_done(now)):
			puzzle_grid.make_shapes_fall()

		#delay for shapes falling
		if (puzzle_grid.one_space_fall_done(now)):
			puzzle_grid.make_shapes_fall()

		#delay finished after attack was made (for sprite animation)
		if (active_character.attack_delay_done(now)):
			#apply skill/attack's effects
			active_character.attack(active_character.current_target, active_character.current_action)

			#next person's turn
			rotation_counter += 1
			active_character = turn_rotation[rotation_counter % character_num]
			someone_is_attacking = False
	
	#update screen
	update_screen()

	pygame.display.update()
	end = time.time()
	diff = end - start
	framerate = 30
	delay = 1.0 / framerate - diff
	if delay > 0:
		time.sleep(delay)



