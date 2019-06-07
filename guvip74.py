try:
	m1,m2=map(int,input().split())
	print(pow(m1,m2))
except ValueError:
	print("invalid")