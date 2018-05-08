import pygame
from pygame.locals import *
from sprites import *

class Dialogue:
	def __init__(self):
		self.which_scenario = 0
		self.dialogue_counter = 0
		self.scenarios = []
		self.bubbles = []
		self.current_character = 0
	
	def add_bubble(self,image):
		self.bubbles.append(image)

	def add_scenario(self,scene):
		self.scenarios.append(scene)

	def draw(self,screen):
		self.current_character = self.scenarios[self.which_scenario][self.dialogue_counter][0]
		self.bubbles[self.current_character].draw(screen,(0,0))

		bit_8_font = pygame.font.Font("Assets/Fonts/8_bit_pusab.ttf", 13)
		skill_text_1 = bit_8_font.render(self.scenarios[self.which_scenario][self.dialogue_counter][1], False, (255, 255, 255))
		screen.blit(skill_text_1, (95,540))

	def detect_click(self, mouse_posx, mouse_posy):
		print (len(self.scenarios[self.which_scenario]))
		if self.bubbles[self.current_character].rect.collidepoint(mouse_posx, mouse_posy):
			if self.dialogue_counter < len(self.scenarios[self.which_scenario])-1 :
				self.dialogue_counter = self.dialogue_counter + 1
				return False
			else:
				return True
			


dialogue = Dialogue()

#0 : Bunny
#1 : Skeleton

scene_1 = [
	(0,"Hello"),
	(1,"This is a test of the dialogue"),
	(0,"This is an interesting story")
]

scene_2 = [
	(0,"Yes"),
	(1,"I agree."),
	(0,"This is very interesting")
]

dialogue.add_bubble(Sprite.image(pygame.image.load("Assets/Story/dialogue_bunny_skel.png"),"window1"))
dialogue.add_bubble(Sprite.image(pygame.image.load("Assets/Story/dialogue_skel_bunny.png"),"window2"))

dialogue.add_scenario(scene_1)
dialogue.add_scenario(scene_2)