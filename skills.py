#contains the skill definitions used by characters in the game

#Bunny skills, returns what happened (string)
def skill_1(attacker, target):
	attacker.puzzle_grid.collected_shapes[0] -= 1
	target.health -= 20
	return attacker.name + " used skill_1 on " + target.name + ", it dealt 20 damage and cost 1 red gem"

#AI skills, returns what happened (string)
def AI_skill_1(attacker, target):
	target.health -= 8
	return attacker.name + " hit " + target.name + " with a sword, it dealt 14 damage"