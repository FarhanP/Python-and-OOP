def gen():
	x=1
	print("This number is printed first")
	yield x

	x+=1
	print("This number is printed second")
	yield x

	x+=1
	print("This number is printed Third")
	yield x
	
c=gen()
next(c)













# # Functions as arguments
# def inc(x):
# 	return x+1
# def dec(x):
# 	return x-1

# def operation(func,a):
# 	result=func(a)
# 	return result

# print(operation(inc,2))