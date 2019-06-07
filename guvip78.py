try:
	num1,num2=map(int,input().split())
	arr1=list(map(int,input().split()))
	arr2=list(map(int,input().split()))
	b=arr1+arr2
	b=sorted(b)
	print(*b)
except ValueError:
	print("invalid")
