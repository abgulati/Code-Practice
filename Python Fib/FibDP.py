import time

fibValues = [0,1]

#wrapper function
def timeKeeper(coreLogic):
	def wrapper():
		start_time = time.time()
		coreLogic()
		print("program executed in:", (time.time() - start_time), " seconds")
	return wrapper

def fib(n):
	for i in range(2,n):
		temp = (fibValues[i-1] + fibValues[i-2])
		fibValues.append(temp)

@timeKeeper
def coreLogic():
	fib(x)

def printFibSeq():
	for i in range(0,x):
		print(fibValues[i])

x = input("Enter length of desired sequence: ")
x = int(x)
coreLogic()
printFibSeq()