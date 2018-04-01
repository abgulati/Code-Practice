def fib():
	v1 = 0
	v2 = 1

	for x in range(0,seq_len):
		print(v1)

		temp = v1
		v1 = v2
		v2 = v2 + temp

seq_len = input("How many digits of the sequence do you want printed?")
seq_len = int(seq_len)

fib()