try:
	num1,num2,num3=map(int,input().split())
	ar=list(map(int,input().split()))
	a=[]
	for i in range(num2-1,num3):
		a.append(ar[i])
	print(min(a))
except ValueError:
	print("invalid")