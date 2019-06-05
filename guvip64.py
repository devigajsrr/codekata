try:
	n1,n2=map(int,input().split())
	arr=list(map(int,input().split()))
	a=[]
	for i in range(0,n1):
		if(arr[i]<n2):
			a.append(arr[i])
	a.sort()
	for i in range(0,len(a)):
		print(a[i],end=" ")
except ValueError:
	print("invalid")
