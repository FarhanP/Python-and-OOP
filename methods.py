class dragonball:

 	def __init__(self,name):
 		self.name=name
 		self.health=100
 		self.damage=10

 	def attack(self,opponent):
 		opponent.health-=self.damage   # opponent's health is damaged by defined points ----> 100-10=90 (updated opponent's health)
hero=dragonball("goku")
villain=dragonball("cell")

print(hero.name)
print(villain.name)
villain.attack(hero)    # object.methodname(object)=====> means hero attacking villain

print(hero.health)   # Prints the villain's health after getting attacked.
