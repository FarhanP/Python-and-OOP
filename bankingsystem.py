from abc import abstractmethod,ABCMeta
import random
class Account(metaclass=ABCMeta):
	@abstractmethod	
	def create_account():
		pass
	@abstractmethod
	def authenticate():
		pass
	@abstractmethod
	def withdraw():
		pass
	@abstractmethod
	def deposit():
		pass
	@abstractmethod
	def display():
		pass




class Savingsaccount(Account):
	def __init__(self):
		self.savingsaccounts={}

	def create_account(self,name,initial_deposit):
		self.account_number=random.randint(10000,99999)
		self.savingsaccounts[self.account_number]=[name,initial_deposit]
		print("Account creation has been successful",self.account_number)
	def authenticate(self,name,account_number):
		if account_number in self.savingsaccounts.keys():
			if self.savingsaccounts[self.account_number][0]==name:
				print("Authentication successful!")
				self.account_number=account_number
				return True
			else:
				print("Authentication Failed!")
				return False
		else:
			print("Authentication Failed!")
			return False

	def withdraw(self,withdrawal):
		if withdrawal>self.savingsaccounts[self.account_number][1]:
			print("Insufficient Balance!")
		else:
			self.savingsaccounts[self.account_number][1]-=withdrawal
			self.display()
	def deposit(self,deposit_amt):
		self.savingsaccounts[self.account_number][1]+=deposit_amt
		self.display()
	def display(self):
		print("Avail Balance:", self.savingsaccounts[self.account_number][1])
	def displayall(self):
		return "list of all accounts:".format(self.savingsaccounts)



savingsaccounts=Savingsaccount()
while True:
	print("1.Enter this option to create a new account")
	print("2.Enter this option to open an existing account")
	print("3.Quit")
	choice=int(input())
	if choice is 1:
		name=input("Enter your name:")
		initial_deposit=int(input("Enter your initial_deposit:"))
		savingsaccounts.create_account(name,initial_deposit)
	elif choice is 2:
		name=input("Enter your name:")
		account_number=int(input("Enter your account_number:"))
		authentication=savingsaccounts.authenticate(name,account_number)
		if authentication==True:
			while True:
				print("1.Enter the option to withdraw")
				print("2.Enter the option to deposit")
				print("3.Enter this option to display")
				print("4.Enter to display the list of accounts")
				print("5.Back to previous menu")
				choice=int(input())
				if choice is 1:
					withdraw=int(input("Enter the amount to withdraw:"))
					savingsaccounts.withdraw(withdraw)
				elif choice is 2:
					deposit=int(input("Enter the amount to deposit:"))
					savingsaccounts.deposit(deposit)
				elif choice is 3:
					savingsaccounts.display()
				elif choice is 4:
					savingsaccounts.displayall()
				elif choice is 5:
					break

	elif choice is 3:
		quit()



















	




