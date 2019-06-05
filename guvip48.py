try:
	n=int(input())
	arr=[]
	for iter in range(1,n+1):
		if(n%iter==0):
			arr.append(iter)
	for i in range (0,len(arr)):
		if(arr[i]%2==1):
			print(arr[i],end=" ")
		else:
			continue
except ValueError:
	print("invalid")