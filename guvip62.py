try:
	n=int(input())
	iter=1
	while(n!=0):
		div=n/iter
		if(div%2==1):
			print(iter)
			break
		iter+=1
except ValueError:
	print("invalid")
