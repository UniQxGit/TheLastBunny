#The character that battles in the game

#needs: (empty)
import pygame
from pygame.locals import *
from skills import * #has the skill definitions, ex. skill_1

#assets: (empty)

#for skill icons(small) and battle menu
battle_menu = None
skill_icon_small_1 = None
skill_icon_small_2 = None
skill_icon_small_3 = None
skill_icon_small_4 = None
bit_8_font = None


#character class
class Character:
	def __init__(self, game_screen, name, puzzle_grid, health, sprite, location):

		#for UI
		self.load_assets()
		self.game_screen = game_screen
		self.skill_rects = [0, 0, 0, 0]
		self.status_image = None
		self.status_bar_rect = None
		self.targeted = False
		self.targeted_status_image = None

		#for animations
		self.location = location
		self.sprite = sprite
		self.started_attack_anim = False
		self.attack_animation_time = 1000
		self.current_action = None
		self.current_target = None

		#for logic
		self.name = name
		self.puzzle_grid = puzzle_grid #AI won't have this
		self.health = health
		self.max_health = health
		self.skill_list = [0, 0, 0, 0]
		self.load_skills()

	#load universal UI for all characters
	def load_assets(self):
		global battle_menu
		global skill_icon_small_1, skill_icon_small_2, skill_icon_small_3, skill_icon_small_4
		global bit_8_font

		#load skill list background image
		battle_menu = pygame.image.load("Assets/InGame/battle_menu.png").convert_alpha();

		#load the skill icon images (small)
		skill_icon_small_1 = pygame.image.load("Assets/InGame/Skillicon_small_1.png").convert_alpha()
		skill_icon_small_2 = pygame.image.load("Assets/InGame/Skillicon_small_2.png").convert_alpha()
		skill_icon_small_3 = pygame.image.load("Assets/InGame/Skillicon_small_3.png").convert_alpha()
		skill_icon_small_4 = pygame.image.load("Assets/InGame/Skillicon_small_4.png").convert_alpha()
		#load font for skill icon images (small)
		bit_8_font = pygame.font.Font("Assets/Fonts/8_bit_pusab.ttf", 13)

	#these are the skills for main bunny, will be stored as an array of functions
	def load_skills(self):
		global skill_1, skill_2, skill_3, skill_4
		self.skill_list[0] = skill_1
		self.skill_list[1] = skill_2
		self.skill_list[2] = skill_3
		self.skill_list[3] = skill_4

	def draw_skill_list(self):
		#draw the skill list background
		self.game_screen.blit(battle_menu , (280,550))

		#icon and text positions
		icon_pos_1 = (315,560)
		icon_pos_2 = (315,560+37*1)
		icon_pos_3 = (315,560+37*2)
		icon_pos_4 = (315,560+37*3)
		text_pos_1 = (360, 575)
		text_pos_2 = (360, 575+37*1)
		text_pos_3 = (360, 575+37*2)
		text_pos_4 = (360, 575+37*3)

		#draw the skill icons and name
		self.game_screen.blit(skill_icon_small_1 , icon_pos_1)
		skill_text_1 = bit_8_font.render("AVOID", False, (255, 255, 255))
		self.game_screen.blit(skill_text_1, text_pos_1)

		self.game_screen.blit(skill_icon_small_2 , icon_pos_2)
		skill_text_2 = bit_8_font.render("BE CUTE", False, (255, 255, 255))
		self.game_screen.blit(skill_text_2, text_pos_2)

		self.game_screen.blit(skill_icon_small_3 , icon_pos_3)
		skill_text_3 = bit_8_font.render("SCRATCH", False, (255, 255, 255))
		self.game_screen.blit(skill_text_3, text_pos_3)

		self.game_screen.blit(skill_icon_small_4 , icon_pos_4)
		skill_text_4 = bit_8_font.render("RAGE!!!", False, (255, 255, 255))
		self.game_screen.blit(skill_text_4, text_pos_4)

		#create collision box (can now click skill by its text)
		self.skill_rects[0] = pygame.Rect(text_pos_1, skill_text_1.get_rect().size)
		self.skill_rects[1] = pygame.Rect(text_pos_2, skill_text_2.get_rect().size)
		self.skill_rects[2] = pygame.Rect(text_pos_3, skill_text_3.get_rect().size)
		self.skill_rects[3] = pygame.Rect(text_pos_4, skill_text_4.get_rect().size)

	#returns skill that was picked, returns None if no skill was picked
	def detect_skill_click(self, target, mouse_posx, mouse_posy):

		#check which skill was clicked
		for i in range(len(self.skill_rects)):
			if (self.skill_rects[i].collidepoint(mouse_posx, mouse_posy)):
				return self.skill_list[i]
				#self.start_attack(target, self.skill_list[i])

		return None

	#setup the status bar
	def setup_status_bar_UI(self, status_image, pos, font, text_pos, targeted_status_image):

		#save the values for drawing
		self.status_image = status_image
		self.status_image_pos = pos
		self.status_image_font = font
		self.status_image_text_pos = text_pos
		#this is how it will look when it is clicked
		self.targeted_status_image = targeted_status_image

	#draw the status bar
	def draw_status_bar(self):

		#draw image
		x_pos = self.status_image_pos[0]
		y_pos = self.status_image_pos[1]
		if (self.targeted == False):
			self.game_screen.blit(self.status_image,(x_pos,y_pos))
		else:
			self.game_screen.blit(self.targeted_status_image,(x_pos,y_pos))

		#draw text over the image
		x_font_pos = self.status_image_text_pos[0]
		y_font_pos = self.status_image_text_pos[1]
		health_string = str(self.health) + " / " + str(self.max_health)
		health_text = self.status_image_font.render(health_string, False, (255, 255, 255)) #value should be pulled from a class variable
		self.game_screen.blit(health_text, (x_font_pos, y_font_pos))

		#create collision box for clicking (this is how enemies/allies will be targeted)
		self.status_bar_rect = pygame.Rect((x_pos, y_pos), self.status_image.get_rect().size)

	#draw the sprite of the character on the screen
	def draw_character(self):
		self.sprite.draw(self.game_screen,self.location)

	#show info of this character
	def show_info(self):
		print ("")
		print ("----Character INFO----")
		print ("Character: " + self.name)

		#enemys wont have a puzzle grid
		if (self.puzzle_grid != None):
			print ("Gem score: " + str(self.puzzle_grid.collected_shapes)[1:-1])
			self.puzzle_grid.show_grid()

	#starts the attack animation and sets up delay before applying skill's effects to target
	def start_attack(self, target, skill):
		#play the attack animation
		self.sprite.play("attack", 1)
		self.started_attack_anim = True
		self.time_started_attack = pygame.time.get_ticks()

		#save the action
		self.current_action = skill
		self.current_target = target

	#attack another player with a skill
	def attack(self, target, skill):
		#apply the effect of skill to target
		skill_result = skill(self, target)
		print (skill_result)
		if (target.health <= 0):
			print (target.name + " died")
			target.sprite.play("die", 1)
		print ("")

		#reset variables, character has completed it's action
		self.current_action = None
		self.current_target = None

	#we want to wait for attack animation to finish before inflicting the damage
	def attack_delay_done(self, time_now):
		if (self.started_attack_anim and (time_now - self.time_started_attack >= self.attack_animation_time)):
			self.started_attack_anim = False
			return True
		return False

