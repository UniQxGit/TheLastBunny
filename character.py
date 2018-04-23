#The character that battles in the game

#needs: (empty)
import pygame
from pygame.locals import *

#assets: (empty)

#character class
class Character:
	def __init__(self, game_screen, name, puzzle_grid, health, sprite, location):

		#for UI
		self.game_screen = game_screen

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

	#draw the status bar UI on the game screen
	def status_bar_UI(self, status_image, pos, font, font_pos):

		#draw image
		x_pos = pos[0]
		y_pos = pos[1]
		self.game_screen.blit(status_image,(x_pos,y_pos))

		#draw text over the image
		x_font_pos = font_pos[0]
		y_font_pos = font_pos[1]
		health_string = str(self.health) + " / " + str(self.max_health)
		health_text = font.render(health_string, False, (255, 255, 255)) #value should be pulled from a class variable
		self.game_screen.blit(health_text, (x_font_pos, y_font_pos))

		#save values for updating
		self.status_bar_font_pos = font_pos
		self.status_bar_font = font

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

		#reset variables, character has completed it's action
		self.current_action = None
		self.current_target = None

	#we want to wait for attack animation to finish before inflicting the damage
	def attack_delay_done(self, time_now):
		if (self.started_attack_anim and (time_now - self.time_started_attack >= self.attack_animation_time)):
			self.started_attack_anim = False
			return True
		return False


