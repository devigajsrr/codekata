try:
	num=int(input())
	c=0
	for iter in range(num):
		num1,num2=map(int,input().split())
		if num1<num2:
			c+=1
	print(c)
except ValueError:
	print("invalid")