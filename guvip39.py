try:
	num=int(input())
	key=num
	t=0
	while num>1:
	    if num%2==0:
	        num=num/2
	        t=t+1
	    else:
	        print("no")
	        break
	if (2**t)==key:
	    print("yes")
except ValueError:
    print("invalid")
