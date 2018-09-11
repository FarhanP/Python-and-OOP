from abc import ABCMeta,abstractmethod
class Human(metaclass=ABCMeta):     #e
	@abstractmethod
	def wt(self):
		return 0

class Man(Human):
	wt=90
	def weight(self):
		print("The weight is:",self.wt)

class Woman(Human):
	wt=100
	def weight(self):
		print("The weight is:",self.wt)

man=Man()
woman=Woman()
man.weight()
woman.weight()





