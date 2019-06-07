try:
	m=int(input())
	arr=list(map(int,input().split()))
	c1=0
	c2=0
	for i in range(0,m):
		if(arr[i]%2==0):
			c1+=1
		else:
			c2+=1
	if(c1==1):
		for j in range(0,m):
			if(arr[j]%2==0):
				print(arr[j])
	elif(c2==1):
		for k in range(0,m):
			if(arr[k]%2==1):
				print(arr[k])
except ValueError:
	print("invalid")