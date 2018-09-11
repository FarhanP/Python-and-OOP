# class student:
# 	def __init__(self,name,age,address):
# 		self.name=name
# 		self.age=age
# 		self.address=address
# farhan=student('farhan',23, 'vaniyambadi')
# faizan=student('faizan',20, 'vaniyambadi')

# print(faizan.name)
# print(farhan.age)
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
