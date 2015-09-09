import sys
import random

months = 0
#size of forest N x N 
n = sys.argv[1]

class entity:
	def __init__(self, position):
		self.age = 0
		self.position = position[0:2]
		
class tree(entity):
	def tick(self):
		self.age += 1
		if (self.age >= 12 and self.age < 120 and random.randint(1,10) <= 1) or (self.age >= 120 and random.randint(1,10) <= 2):
			#spawn a sapling on adjacent empty space
			
class lumberjack(entity):
	def move:
		#pick a random spot and see if there is a bear, if not move
	def tick:
		self.age += 1
class bear(entity):
	def tick:
		self.age += 1

def spawnForest:
	pass
	
