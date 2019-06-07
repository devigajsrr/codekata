try:
	num=int(input())
	arr=list(map(int,input().split()))
	b=[]
	if num==1:
		print(arr[0])
	else:
		for i in range(num-1):
			b.append(arr[i]|arr[i+1])
		print(max(b))
except ValueError:
	print("invalid")