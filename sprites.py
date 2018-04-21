#Sprite Mechanics

import pygame
from pygame.locals import *

base_path = "Assets/Characters/"

class Animation:
	#animations = {}
	count = 0
	animation_delay = 50.0


	#Add function for adding in an animation
	#it will look in the folder, and load all frames for parameter "length"
	#the final path will be "base_animation+name+i" for each i to length
	def add_anim(self,animation,length):
		print ("Count: " + str(self.count))
		
		animation_list = []

		for i in range(length):
			animation_name = self.name + "_" + animation + "_" + str(i+1)
			animation_path = base_path+self.name+"/"+animation+"/"
			animation_list.append(pygame.image.load(animation_path+animation_name+".png").convert_alpha())
			print (self.name + " Added " + animation_path + animation_name)
		self.animations[animation] = animation_list
		self.count += 1
		self.rect = ((0,0),(self.animations[animation][0].get_width(),self.animations[animation][0].get_height()))

		

	#base_animation is the folder of animtion i.e "attack".
	#it will look in the folder, and load all frames for parameter "length"
	#the final path will be "base_animation+name+i" for each i to length
	def __init__(self,name,base_animation,length):
		self.name = name
		self.count = 0
		self.current_animation = base_animation
		self.default_animation = base_animation
		self.current_animation = self.default_animation	
		self.last_update = 0.0
		self.last_index = 0
		self.start_time = 0.0
		self.end_time = 0.0
		self.is_playing = False
		self.animations = {}

		self.add_anim(base_animation,length)
		
	#will change the currently playing animation to a specified animation
	#def set_anim(self,animation,length)	

	#call during game loop always play current animation unless overridden by another animation.
	def update(self,screen,position,index):
		if index != self.last_index:
			self.last_update = pygame.time.get_ticks()
		#print (self.name + " is playing" + self.current_animation)
		screen.blit(self.animations[self.current_animation][index], position)
		self.last_index = index
	#call 
	def play(self,screen,animation,count):
		self.start_time = pygame.time.get_ticks()
		self.end_time = self.start_time + (len(self.animations[self.current_animation])*self.animation_delay*count)
		self.is_playing = true
		#while()

class Sprite:
	anim = None
	anim_index = 0
	name = ""

	def __init__(self,anim,name):
		self.anim = anim
		self.anim_index = 0
		self.name = name

	def draw(self,screen,position):
		#print (self.name)
		print (str(self.anim.last_update) + " -> " + str(self.anim_index))
		#print (str(pygame.time.get_ticks() - (self.anim.last_update + self.anim.animation_delay)))
		if self.anim_index >= len(self.anim.animations[self.anim.current_animation]):
			self.anim_index = 0
		self.anim.update(screen,position,self.anim_index)
		if pygame.time.get_ticks() > self.anim.last_update + self.anim.animation_delay:
			self.anim_index += 1
		if self.anim.is_playing and pygame.time.get_ticks() > self.anim.end_time:
			self.anim_index = 0
			self.current_animation = self.anim.default_animation
		


