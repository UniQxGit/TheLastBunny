#The character that battles in the game
#also contains the skill definitions used by characters in the game

#needs: (empty)

#assets: (empty)

#Bunny skills, returns what happened (string)
def skill_1(attacker, target):
	attacker.puzzle_grid.collected_shapes[0] -= 1
	target.health -= 20
	return attacker.name + " used skill_1 on " + target.name + ", it dealt 20 damage and cost 1 red gem"

#AI skills, returns what happened (string)
def AI_skill_1(attacker, target):
	target.health -= 14
	return attacker.name + " hit " + target.name + " with a sword, it dealt 14 damage"

#character class
class Character:
	def __init__(self, game_screen, name, puzzle_grid, health):

		#for UI
		self.game_screen = game_screen

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

	def show_info(self):
		print ("")
		print ("----Character INFO----")
		print ("Character: " + self.name)

		#enemys wont have a puzzle grid
		if (self.puzzle_grid != None):
			print ("Gem score: " + str(self.puzzle_grid.collected_shapes)[1:-1])
			self.puzzle_grid.show_grid()

	def attack(self, target, skill):
		skill_result = skill(self, target)
		print (skill_result)
		if (target.health <= 0):
			print (target.name + " died")

