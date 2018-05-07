#Sprite Mechanics

import pygame
from pygame.locals import *
import math
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
		self.rect = pygame.Rect((0,0),(self.animations[animation][0].get_width(),self.animations[animation][0].get_height()))

		

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

	def __init__(self,name):
		self.name = name
		self.hidden = False
		self.position = (0,0)
		self.image = None

		self.anim = None
		self.anim_index = 0
		self.current_animation = None
		self.default_animation = None
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
		self.return_to_default = True
		self.stopped = False
		self.hide_after = False

	@classmethod
	def animation(self,anim,name):
		sprite = Sprite(name)
		sprite.anim = anim
		sprite.current_animation = anim.current_animation
		sprite.default_animation = anim.default_animation
		sprite.rect = anim.rect;
		return sprite

	@classmethod
	def image(self,image,name):
		sprite = Sprite(name)
		sprite.image = image
		sprite.rect = image.get_rect()
		return sprite


	def draw(self,screen,position):
		self.position = position
		self.rect.x = position[0]
		self.rect.y = position[1]
		if self.anim == None:
			screen.blit(self.image, position)
		else:
			#print (self.name)
			#print (str(self.anim.last_update) + " -> " + str(self.anim_index))
			#print (str(pygame.time.get_ticks() - (self.anim.last_update + self.anim.animation_delay)))
			if self.is_playing:
				if self.anim_started == False:
					self.play_counter = 0
					self.anim_started = True

				if self.play_counter >= self.play_count:
					if self.return_to_default == False:
						self.stopped = True
						self.anim_index = len(self.anim.animations[self.current_animation])-1
					else:
						self.anim_index = 0
						self.current_animation = self.default_animation

					if self.hide_after == True:
						self.hidden = True

					
					self.is_playing = False;
					self.play_counter = 0
					self.anim_started = False
					print ("Done Playing. Returning to " + self.current_animation)
				elif self.stopped == False:
					self.anim_index = self.play_index

			if self.anim_index >= len(self.anim.animations[self.current_animation]):
				self.play_counter += 1
				if self.return_to_default == True:
					self.anim_index = 0

			if self.hidden == False:
				self.update(screen,position,self.anim_index)
		
			if pygame.time.get_ticks() > self.last_update + self.animation_delay and self.stopped == False:
				self.anim_index += 1

	#call during game loop always play current animation unless overridden by another animation.
	def update(self,screen,position,index):
		if index != self.last_index:
			self.last_update = pygame.time.get_ticks()
		
		if self.is_playing:
			if self.play_index >= len(self.anim.animations[self.current_animation]):
				if self.play_counter < self.play_count:
					self.play_index = 0
				else:
					self.play_index = len(self.anim.animations[self.current_animation]) - 1
			index = self.play_index
		print (self.name + " is playing" + self.current_animation)

		print (index)
		screen.blit(self.anim.animations[self.current_animation][index], position)
		self.last_index = index
		
		if self.is_playing and pygame.time.get_ticks() > self.last_update + self.animation_delay and self.stopped == False:
			self.play_index += 1

	#currently not suitable for global use. Only opening splash screen.
	def fade_in(self,screen,duration):
		duration = duration * 1000
		end_time = pygame.time.get_ticks() + (duration)
		delta_time = 0.0
		current_time = pygame.time.get_ticks()
		last_time = pygame.time.get_ticks()
		elapsed_time = 0.0
		alpha = 0

		self.hidden = True
		temp = pygame.Surface((self.image.get_width(), self.image.get_height())).convert()
		temp.blit(screen,self.position)
		temp.blit(self.image,(0,0))

		while alpha < 200:
			for event in pygame.event.get():
				#pressing 'x' on the window
				if (event.type == QUIT):
					pygame.quit()
					exit()
			current_time = pygame.time.get_ticks()
			elapsed_time = elapsed_time + (current_time - last_time)
			
			if last_time != current_time:
				alpha = math.ceil((elapsed_time/duration) * 255)
				temp.set_alpha(alpha)	
				print (math.ceil((elapsed_time/duration) * 255))
			screen.blit(temp,self.position)
			last_time = current_time
			pygame.display.update()
		self.image.set_alpha(255)
		self.hidden = False

	#currently not suitable for global use. Only opening splash screen.
	def fade_out(self,screen,duration):
		duration = duration * 1000
		end_time = pygame.time.get_ticks() + (duration)
		delta_time = 0.0
		current_time = pygame.time.get_ticks()
		last_time = current_time
		elapsed_time = duration
		alpha = 255

		temp = pygame.Surface((self.image.get_width(), self.image.get_height())).convert()
		temp.blit(screen,self.position)
		temp.blit(self.image,(0,0))

		self.hidden = True
		while alpha > 50:
			for event in pygame.event.get():
				#pressing 'x' on the window
				if (event.type == QUIT):
					pygame.quit()
					exit()
			current_time = pygame.time.get_ticks()
			elapsed_time = elapsed_time - (current_time - last_time)
			
			if last_time != current_time:
				alpha = math.ceil((elapsed_time/duration) * 255)
				print (alpha)
				temp.set_alpha(alpha)

			screen.fill((0,0,0))
			screen.blit(temp,self.position)
			last_time = current_time
			pygame.display.update()
		self.image.set_alpha(0)
		self.hidden = False

	def play(self,animation,count):
		self.start_time = pygame.time.get_ticks()
		self.play_count = count
		self.is_playing = True
		self.stopped = False
		self.hidden = False
		self.current_animation = animation
		self.play_index = 0
		print ("Play " + animation + str(count) + " Times")