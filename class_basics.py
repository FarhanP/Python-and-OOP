# A class is used to logically group data and functions to re-use easily and to build upon.
# A class also describes object behavior
# Objects are the instances/member of the class. Object has a state (behaving,properties)
# data and functions are referred to as data-->ATTRIBUTES and functions-->METHODS
# A function inside class is known as METHODS
# Instance variables are unique to each instances(objects) in the class
class Employee:   			 					# class structure named Employee, class is like a blueprint for objects/instances
		no_of_emps=0
		raise_amount=1.05						# class variable are variables that are shared among all the instances of the class.
		def __init__(self, first,last,pay):  	# Known as initialize method also known as a constructor in other languages like java. 
				self.first=first				# when we create methods inside a class, they receive instances(objects) as a first argumemt automatically.conventional is to use 'self'. It doesn't have to be 'self'
				self.last=last			 		# We can use 'pass'inside the class which means do nothing
				self.pay=pay
				self.email=first+last+"@gamil.com"
				Employee.no_of_emps+=1			# we increment this here because init method runs every time when an object is created(creating new employee)
												# we don't use self here as no.of employees is not going to be unique for each instances. Just class.
		@property										
		def fullname(self):
				return "{} {}".format(self.first,self.last)  # self is used here on first and lastname so that it will work with all instances

		def apply_raise(self):
				self.pay= int(self.pay*self.raise_amount)	# we can access class variables using class itself or its instances


emp1=Employee("Mohamed","Farhan",50000)   			# emp1 is an object of class Employee
						    						# each of these objects have attributes unique to them
emp2=Employee("Test","User",60000)     				# both are unique instances(objects) to the class

# emp1.firstname="Mohamed"	#Manually creating instance variable
# emp1.lastname="Farhan"b
# emp1.email="pmdfarhan@gmail.com"  
# emp1.pay=50000

# emp2.firstname="Test"	#Manually creating instance variable
# emp2.lastname="User"
# emp2.email="Testuser@gmail.com"
# emp2.pay=50000
# print(Employee.fullname(emp1))  #classname.method(object/instances)--> here we have to pass instances manually 
# print(emp1.email)  				#both objects are unique
# print(emp2.email)
# print(emp1.fullname())	
# print(Employee.__fullname__())	
emp1.apply_raise()
# print(Employee.fullname(emp1))
print(emp1.fullname)
# print(emp2.fullname())
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)
# print(emp1.raise_amount)   		#accessing class variables using its instances
# print(Employee.raise_amount)	#accessing class variables using the class itself
# print(emp1.__dict__)			# refer the output for this, the instances actually don't have class variables
# print(Employee.__dict__)		# refer the output for this, the class do have class variables(obvious)
# Employee.raise_amount=1.5           # assigning the new value for the class
# emp1.raise_amount=1.6   			# assigning the new value for the instances, values are changed only for instances
# print(emp1.raise_amount)
# print(Employee.raise_amount)
# print(emp1.no_of_emps)
# print("{} {}".format(emp1.first,emp1.last))--->printing out a emp's full name which is a tedious process with this method



# help(dict)

class country:
	def __init__(self,name,population,area):

		self.name=name
		self.population=population
		self.are=area
	def __repr__(self):								# To see the representation of the object
		return repr((self.name,self.population)) 	# Extra parenthesis to return as a tuple



countries=[country('india','1.2B',2000),country('china','2B',8000),country('japan','115k',1000)]  #list


print(countries[0:2])			#list slicing