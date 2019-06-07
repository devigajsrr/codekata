try:	
	n1,n2=map(int,input().split())
	arr=list(map(int,input().split()))
	for i in range(0,n1-n2):
		print(arr[i],end=" ")
except ValueError:
	print("invalid")