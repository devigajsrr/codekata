try:
	n=int(input())
	arr=list(map(int,input().split()))
	a=[]
	for i in range(0,n-1):
		if(arr[i]>arr[i+1]):
			a.append(arr[i])
		else:
			a.append(arr[i+1])
	for j in range(0,len(a)):
		print(a[j],end=" ")
except ValueError:
	print("invalid")
