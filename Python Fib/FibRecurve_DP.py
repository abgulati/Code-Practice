import time

fibDict = {0: 0, 1: 1}

def timeKeeper(coreLogic):

	def wrapper():
		start_time = time.time()
		coreLogic()
		print("Program executed in:", (time.time() - start_time), " seconds")
	return wrapper

def fib(n):
	
	if n in fibDict:
		return fibDict[n]
	else:
		temp = (fib(n-2) + fib(n-1))
		fibDict[n] = temp
		return temp

@timeKeeper
def coreLogic():
	for i in range(x,0,-1):
		temp = fib(i)
		print(temp)

x = input("Enter length of desired sequence: ")
x = int(x)
coreLogic()