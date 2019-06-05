try:
	num1,num2=map(int,input().split(" "))
	c=0
	for iter in range(num1,num2+1):
		for j in range(1,iter+1):
			if j**2==iter:
				c+=1
	print(c)
except ValueError:
	print("invalid")
