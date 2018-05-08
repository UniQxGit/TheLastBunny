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

		bit_8_font_small = pygame.font.Font("Assets/Fonts/8_bit_pusab.ttf", 13)
		bit_8_font_large = pygame.font.Font("Assets/Fonts/8_bit_pusab.ttf", 18)
		skill_text_1 = bit_8_font_large.render(self.bubbles[self.current_character].name, False, (255, 255, 255))
		skill_text_2 = bit_8_font_small.render(self.scenarios[self.which_scenario][self.dialogue_counter][1], False, (255, 255, 255))
		screen.blit(skill_text_1, (90,495))
		screen.blit(skill_text_2, (90,540))

	def detect_click(self, mouse_posx, mouse_posy):
		print (len(self.scenarios[self.which_scenario]))
		if self.bubbles[self.current_character].rect.collidepoint(mouse_posx, mouse_posy):
			if self.dialogue_counter < len(self.scenarios[self.which_scenario])-1 :
				self.dialogue_counter = self.dialogue_counter + 1
				return False
			else:
				return True
			


dialogue = Dialogue()

#0 : EMPTY
#1 : Bunny
#2 : BUNNYVILLE CIVILIANS
#3 : Dying Civilian
#4 : Skeleton

scene_1 = [
	(0,"(RUMBLE RUMBLE)"),
	(1,"What's that?  ..Am I dreaming? What's happening to the sky?"),
	(2,"*SCREEEAM!!!!!!*"),
	(4,"(Munch Munch)"),
	(2,"Y- ... You"),
	(2,"YOU ATE HIM!!"),
	(2,"WHY??!!"),
	(4,"..hungry..."),
	(2,"But you don't even have a digestive system!!"),
	(1,"What..? Skeletons?"),
	(0,"(A dying civilian clings to bunny's leg..)"),
	(3,"p-please.. help .. me.."),
	(1,"I.. I have to hide.. I need to get out of here!"),
	(0,"(...)"),
	(0,"(Hours Later...)"),
	(0,"(The stench of blood fills the air)"),
	(1,"They're.. gone.."),
	(1,"Every last one of them.."),
	(1,"I'LL KILL YOU ALL!!!!"),
	(4,"(silence)")
]

scene_2 = [
	(0,"Yes"),
	(1,"I agree."),
	(0,"This is very interesting")
]

dialogue.add_bubble(Sprite.image(pygame.image.load("Assets/Story/dialogue_empty.png"),""))
dialogue.add_bubble(Sprite.image(pygame.image.load("Assets/Story/dialogue_bunny_skel.png"),"BUNNY"))
dialogue.add_bubble(Sprite.image(pygame.image.load("Assets/Story/dialogue_empty.png"),"BUNNYVILLE CIVILIANS"))
dialogue.add_bubble(Sprite.image(pygame.image.load("Assets/Story/dialogue_empty.png"),"DYING CIVILIAN"))
dialogue.add_bubble(Sprite.image(pygame.image.load("Assets/Story/dialogue_skel_bunny.png"),"SKELETON"))

dialogue.add_scenario(scene_1)
dialogue.add_scenario(scene_2)