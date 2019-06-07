try:
	m=int(input())
	factorial=1
	for iter in range(1,m+1):
		factorial*=iter
	print(factorial)
except ValueError:
	print("invalid")