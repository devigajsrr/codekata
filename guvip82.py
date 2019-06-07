try:
	m=int(input())
	arr=list(map(int,input().split()))
	for i in range(0,len(arr)):
	    if m==1:
	        print(arr[i])
	        break
	    elif arr[i]==arr[i+1]:
	        print(arr[i])
	        break
	    else:
	        print("0")
	        break
except ValueError:
	print("invalid")