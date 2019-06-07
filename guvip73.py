try:
	m1,m2=map(int,input().split())
	arr=list(map(int,input().split()))
	for i in range(0,m1):
		if(arr[i]==m2):
			print(i+1)
except ValueError:
	print("invalid")