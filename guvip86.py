try:
	m=int(input())
	arr=[int(m) for m in input().split()]
	for i in range(0,len(arr)-1):
	    xor=arr[i]^arr[i+1]
	print(xor)
except ValueError:
	print("invalid")
