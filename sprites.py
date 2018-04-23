#Sprite Mechanics

import pygame
from pygame.locals import *

base_path = "Assets/Characters/"

class Animation:
	#animations = {}
	


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
		self.animations = {} #dictionary. (Key[string],value)
		self.current_animation = base_animation
		self.default_animation = base_animation
		self.current_animation = self.default_animation	

		self.add_anim(base_animation,length)
		
	#will change the currently playing animation to a specified animation
	#def set_anim(self,animation,length)	

	#call 
		#while()

class Sprite:
	animation_delay = 50.0

	def __init__(self,anim,name):
		self.anim = anim
		self.anim_index = 0
		self.name = name
		self.play_counter = 0
		self.is_playing = False
		self.last_update = 0.0
		self.last_index = 0
		self.start_time = 0.0
		self.end_time = 0.0
		self.is_playing = False
		self.play_count = 0
		self.play_index = 0
		self.anim_started = False
		self.current_animation = anim.current_animation
		self.default_animation = anim.default_animation
		self.return_to_default = True
		self.stopped = False

	def draw(self,screen,position):
		#print (self.name)
		#print (str(self.anim.last_update) + " -> " + str(self.anim_index))
		#print (str(pygame.time.get_ticks() - (self.anim.last_update + self.anim.animation_delay)))
		if self.is_playing:
			if self.anim_started == False:
				self.play_counter = 0
				self.anim_started = True

			if self.play_counter >= self.play_count:
				self.anim_index = 0
				self.current_animation = self.default_animation
				self.is_playing = False;
				self.play_counter = 0
				self.anim_started = False
				print ("Done Playing. Returning to " + self.current_animation)
				if self.return_to_default == False:
					self.stopped = True
			else:
				self.anim_index = self.play_index

		if self.anim_index >= len(self.anim.animations[self.current_animation]):
			self.anim_index = 0
			self.play_counter += 1

		if self.stopped == False:
			self.update(screen,position,self.anim_index)
	
		if pygame.time.get_ticks() > self.last_update + self.animation_delay:
			self.anim_index += 1

	#call during game loop always play current animation unless overridden by another animation.
	def update(self,screen,position,index):
		if index != self.last_index:
			self.last_update = pygame.time.get_ticks()
		
		if self.is_playing:
			if self.play_index >= len(self.anim.animations[self.current_animation]):
				self.play_index = 0
			index = self.play_index
		#print (self.name + " is playing" + self.current_animation)

		screen.blit(self.anim.animations[self.current_animation][index], position)
		self.last_index = index
		
		if self.is_playing and pygame.time.get_ticks() > self.last_update + self.animation_delay:
			self.play_index += 1

	def play(self,animation,count):
		self.start_time = pygame.time.get_ticks()
		self.play_count = count
		self.is_playing = True
		self.current_animation = animation
		self.play_index = 0
		print ("Play " + animation + str(count) + " Times")