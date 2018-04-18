#Sprite Mechanics

import pygame
from pygame.locals import *

gems_path = "Assets/Characters/"

class Sprite:
	rect = None
	base_image = None

	def __init__(self,base_animation,length):
		
