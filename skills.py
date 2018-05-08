#contains the skill definitions used by characters in the game

#skill costs right now are hard coded
skill_1_cost = 5
skill_2_cost = 0
skill_3_cost = 3
skill_4_cost = 4 #minimum of 4, but will use it all

#Bunny skills, returns what happened (string)

#will make target miss their attack on bunny in next turn
def skill_1(attacker, target):
	attacker.puzzle_grid.collected_shapes[0] -= skill_1_cost
	target.avoid_debuff = True
	return attacker.name + " used avoid on " + target.name

#restores 20 health. the more gems the bunny currently has, the more it heals
def skill_2(attacker, target):
	heal_amt = 10 + (attacker.puzzle_grid.collected_shapes[1] * 2)

	attacker.puzzle_grid.collected_shapes[1] -= skill_2_cost
	attacker.health += heal_amt
	return attacker.name + " used his cuteness, somehow he healed for " + str(heal_amt)

#deal 10 base damage. the more gems the bunny currently has, the more damage it does
def skill_3(attacker, target):
	total_dmg = 10 + (1 * attacker.puzzle_grid.collected_shapes[2])

	attacker.puzzle_grid.collected_shapes[2] -= skill_3_cost
	target.health -= 10
	return attacker.name + " used scratch on " + target.name + ", it dealt " + str(total_dmg) + " damage"

#needs minimum 4 greens. if more bunny will use it all. the more used the higher the damage
def skill_4(attacker, target):
	cost = attacker.puzzle_grid.collected_shapes[3]
	total_dmg = attacker.puzzle_grid.collected_shapes[3] * 6

	target.health -= total_dmg
	attacker.puzzle_grid.collected_shapes[3] = 0
	return attacker.name + " used rage on " + target.name + ", it dealt " + str(total_dmg) + "  damage"

#AI skills, returns what happened (string)
def AI_skill_1(attacker, target):

	#check if main bunny used 'avoid' on AI
	if (attacker.avoid_debuff == True):
		attacker.avoid_debuff = False
		return attacker.name + "'s attack missed, " + target.name + " avoided it"

	target.health -= 8
	return attacker.name + " hit " + target.name + " with a sword, it dealt 14 damage"