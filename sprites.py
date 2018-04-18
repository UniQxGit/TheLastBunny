#Sprite Mechanics

import pygame
from pygame.locals import *

gems_path = "Assets/Characters/"

class Sprite:
	rect = None
	base_image = None
	
	#base_animation is the folder of animtion i.e "attack".
	#it will look in the folder, and load all frames for parameter "length"
	#the final path will be "base_animation+name+i" for each i to length
	def __init__(self,base_animation,name,length):
		for i in range(length):
			

	#Add function for adding in an animation
	#it will look in the folder, and load all frames for parameter "length"
	#the final path will be "base_animation+name+i" for each i to length
	#def add_anim(self,animation,length)
