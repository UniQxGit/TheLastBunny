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
from dialogue import *
import math
import time

#pygame setup
pygame.init()
pygame.display.set_caption("The Last Bunny")
screen = pygame.display.set_mode((1280,720))#,pygame.FULLSCREEN)
bg = [ Sprite.image(pygame.image.load("Assets/opening.png").convert(),"bg_0"),
	Sprite.image(pygame.image.load("Assets/Story/bg_1.png").convert(),"bg_1"),
	Sprite.image(pygame.image.load("Assets/InGame/Level_1.png").convert(),"bg_2"),
	Sprite.image(pygame.image.load("Assets/Story/bg_1.png").convert(),"bg_1")
]



w, h = pygame.display.get_surface().get_size()

#-----LevelAssets-----

#music
music = ["Assets/Music/opening.mp3","Assets/Music/cutscene.mp3","Assets/Music/battle.mp3","Assets/Music/cutscene.mp3"]
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
dark_overlay = Sprite.image(pygame.image.load("Assets/Story/dark_overlay.png"),"play")
black = Sprite.image(pygame.image.load("Assets/black.png").convert(),"black")
battle_skill_overlay = Sprite.image(pygame.image.load("Assets/InGame/battle_skill_overlay.png").convert_alpha(),"Battle Menu")
feedback_window = Sprite.image(pygame.image.load("Assets/InGame/Status_overlay.png").convert_alpha(),"feedback UI")
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
black.fade_in(screen,5.0)

#opening Animation
opening_bright = Sprite.image(pygame.image.load("Assets/bright_sky.png").convert(),"bright")
opening_dark = Sprite.image(pygame.image.load("Assets/dark_sky.png").convert(),"dark")
opening = Sprite.image(pygame.image.load("Assets/opening.png").convert(),"opening")
intro_bunny = Sprite.image(pygame.image.load("Assets/Opening/Bunny.png").convert_alpha(),"intro_bunny")

end = pygame.time.get_ticks() + 3000
opening_bright.fade_in(screen,5.0) 
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

def switch_scene(scene):
	global which_scene
	if which_scene == scene:
		return

	black.fade_in(screen,5.0)
	which_scene = scene
	pygame.mixer.music.load(music[which_scene])
	pygame.mixer.music.play(-1)
	
	bg[which_scene].fade_in(screen,7.0) #redraw background

	if which_scene == 1:
		dialogue.dialogue_counter = 0
		dialogue.which_scenario = 0
		dark_overlay.draw(screen,(0,0))
		pygame.display.update()
		pygame.time.delay(3000)
			#black.fade_out(screen,5.0)	
	if which_scene == 2:
		reset_level()
	if which_scene == 3:
		dialogue.dialogue_counter = 0
		dialogue.which_scenario = 1
		dark_overlay.draw(screen,(0,0))
		pygame.display.update()
		pygame.time.delay(3000)




#turn taking
failed = False
turn_rotation = [main_bunny, enemy_1, enemy_2, enemy_3]
character_num = 4
enemy_num = 3
rotation_counter = 4
active_character = turn_rotation[rotation_counter % character_num] #this will go from 0 -> 4
someone_is_attacking = False
if (turn_rotation[0] == main_bunny):
	can_click_grid = True
else:
	can_click_grid = False

#target picking
skill_picked = None
targeted_character = enemy_1
enemy_1.targeted = True
def pick_target (mouse_posx, mouse_posy):
	global turn_rotation, targeted_character
	found_target = False

	for character in turn_rotation:
		if (character.status_bar_rect.collidepoint(mouse_posx, mouse_posy)):
			targeted_character.targeted = False
			character.targeted = True
			targeted_character = character
			found_target = True


	# if (found_target == False):
	# 	targeted_character = None

#text in a box UI, give the user messages on their actions
feedback_message = "hello"
def feedback_message_UI():
	global feedback_message,screen

	feedback_window.draw(screen,(158,475))

	font = pygame.font.Font("Assets/Fonts/8_bit_pusab.ttf", 10)
	words = [word.split(' ') for word in feedback_message.splitlines()]  # 2D array where each row is a list of words.
	space = font.size(' ')[0]  # The width of a space.
	boundary = 20
	max_width, max_height = feedback_window.rect.size
	pos = (185, 490)
	x, y = pos

	for line in words:
		for word in line:
			word_surface = font.render(word, 0, (255, 255, 255))
			word_width, word_height = word_surface.get_size()
			if x + word_width >= pos[0]+(max_width - boundary) :
				x = pos[0]  # Reset the x.
				y += word_height  # Start on new row.
			screen.blit(word_surface, (x, y))
			x += word_width + space
		x = pos[0]  # Reset the x.
		y += word_height  # Start on new row.

def reset_level():
	puzzle_grid.collected_shapes = [0,0,0,0]
	for character in turn_rotation:
		character.health = character.max_health
		character.return_to_default = True
		character.sprite.play("idle",1)
	failed = False

#update the screen with the new changes, this will be called at the end part of the game loop
def update_screen():
	global can_splash,screen,targeted_character
	if which_scene == 0:
		play_button.draw(screen,(450,315))
		quit_button.draw(screen,(450,460))
	elif which_scene == 1:
		dark_overlay.draw(screen,(0,0))
		dialogue.draw(screen)
	elif which_scene == 2:
		#update status bar UI for all characters
		global main_bunny
		global enemy_1,enemy_2,enemy_3
		global level 
		global enemy_num
		global failed
		global turn_rotation
		#Level
		screen.blit(level,(133,175))

		if targeted_character != None and targeted_character.health <= 0:
			
			targeted_character = None

			for character in turn_rotation:
				if character.health > 0 and character != main_bunny:
					targeted_character = character
					character.targeted = True
					break

			enemy_num = enemy_num - 1
			if enemy_num <= 0:
				switch_scene(3)

		if main_bunny.health <= 0 and failed == False and main_bunny.sprite.is_playing == False:
			pygame.time.delay(3000)
			switch_scene(1)
			failed = True


		main_bunny.draw_status_bar()
		if enemy_1.health > 0:
			enemy_1.draw_status_bar()
		if enemy_2.health > 0:
			enemy_2.draw_status_bar()
		if enemy_3.health > 0:
			enemy_3.draw_status_bar()

		#update the grid
		global puzzle_grid
		puzzle_grid.draw_grid(710,133)

		#update the sprites
		main_bunny.draw_character()
		enemy_1.draw_character()
		enemy_2.draw_character()
		enemy_3.draw_character()
		battle_skill_overlay.draw(screen,battle_skill_overlay.position)
		#update the skill battle menu
		main_bunny.draw_skill_list()

		#update feedback message
		feedback_message_UI()
	elif which_scene == 3:
		dialogue.draw(screen)

# #game loop
while (True):
	start = time.time()
	#Draw UI
	
	#if Level 1
	screen.blit(bg[which_scene].image ,(0,0)) #redraw background

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

	#tell user current status
	if (active_character == main_bunny and 
		someone_is_attacking == False and 
		which_scene > 1):

		if (main_bunny.feedback_message != ""):
			feedback_message = main_bunny.feedback_message
		elif (main_bunny.puzzle_grid.finished_grid_move == False):
			feedback_message = "pop a shape on the grid"
		elif (targeted_character == None):
			feedback_message = "pick a target"
		elif (skill_picked == None):
			feedback_message = "pick a skill"


	#check user input
	for event in pygame.event.get():
		#pressing 'x' on the window
		if (event.type == QUIT):
			pygame.quit()
			exit()

		mouse_posx, mouse_posy = pygame.mouse.get_pos()


		if which_scene == 2:
			battle_skill_overlay.position = (-battle_skill_overlay.rect.w,-battle_skill_overlay.rect.h)
			if main_bunny.puzzle_grid.finished_grid_move != None:
				for i in range(len(main_bunny.skill_rects)):
					if (main_bunny.skill_rects[i].collidepoint(mouse_posx, mouse_posy)):
						battle_skill_overlay.position = (main_bunny.skill_rects[i].x,main_bunny.skill_rects[i].y)



		#mouse was clicked
		if event.type == pygame.MOUSEBUTTONDOWN:
			

			#possible improvement: can make this cleaner by checking detection first for skill picking
			#check if it's our turn and no one is currently doing an attack animation
			if (event.button == 1):
				if (which_scene == 0):
					if (play_button.rect.collidepoint(mouse_posx, mouse_posy)):
						switch_scene(1)
					elif (quit_button.rect.collidepoint(mouse_posx, mouse_posy)):
						pygame.quit()
						exit()
				elif (which_scene == 1):
					if dialogue.detect_click(mouse_posx,mouse_posy):
						switch_scene(2)
				elif (which_scene == 3):
					if dialogue.detect_click(mouse_posx,mouse_posy):
						switch_scene(0)
				if (active_character == main_bunny and someone_is_attacking == False and which_scene == 2):
					main_bunny.feedback_message = ""

					#step 1: click on grid
					if main_bunny.puzzle_grid.finished_grid_move == False:
						puzzle_grid.detect_shape_click(mouse_posx, mouse_posy)

					#step 3: click skill
					if targeted_character != None:
						skill_picked = main_bunny.detect_skill_click(targeted_character, mouse_posx, mouse_posy)
						feedback_message = main_bunny.feedback_message

						#start attack
						if (skill_picked != None):
							main_bunny.start_attack(targeted_character, skill_picked)
							feedback_message = "starting attack..."

							#reset values
							someone_is_attacking = True
							skill_picked = None
							main_bunny.puzzle_grid.finished_grid_move = False
							main_bunny.puzzle_grid.disable_grid = False
							

					#step 2: click target
					if main_bunny.puzzle_grid.finished_grid_move == True and skill_picked == None:
						pick_target(mouse_posx, mouse_posy)

	if which_scene == 2:
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
			feedback_message = active_character.feedback_message

			#next person's turn
			rotation_counter += 1
			active_character = turn_rotation[rotation_counter % character_num]
			someone_is_attacking = False
			main_bunny.feedback_message = ""
	
	#update screen
	update_screen()

	pygame.display.update()
	end = time.time()
	diff = end - start
	framerate = 30
	delay = 1.0 / framerate - diff
	if delay > 0:
		time.sleep(delay)



