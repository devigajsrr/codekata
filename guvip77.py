try:
	m=int(input())
	arr=list(map(int,input().split()))
	count=1
	a=[]
	for i in range(0,m-1):
		if(arr[i]<arr[i+1]):
			count+=1
		else:
			a.append(count)
			count=1
	a.append(count)
	print(max(a))
except ValueError:
	print("invalid")