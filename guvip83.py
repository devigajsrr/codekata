try:
	num=int(input())
	arr=[int(x) for x in input().split()]
	b=arr[0]
	for i in range(1,len(arr)):
		b=b|arr[i]
	print(b)
except ValueError:
	print("invalid")