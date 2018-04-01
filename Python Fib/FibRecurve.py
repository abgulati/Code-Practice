import time

def timeKeeper(coreLogic):

	def wrapper():
		start_time = time.time()
		coreLogic()
		print("Program executed in:", (time.time() - start_time), " seconds")
	return wrapper

def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1

	return (fib(n-2) + fib(n-1))

@timeKeeper
def coreLogic():
	for i in range(x,0,-1):
		temp = fib(i)
		print(temp)

x = input("Enter length of desired sequence: ")
x = int(x)
coreLogic()