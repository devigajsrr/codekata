try:
	arraysize,sum=map(int,input().split())
	arr=[int(x) for x in input().split()]
	for i in range(0,arraysize):
		for j in range(i+1,arraysize):
			if arr[i]+arr[j]==sum:
				print("yes")
				exit(0)
	print("no")
except ValueError:
	print("invalid")