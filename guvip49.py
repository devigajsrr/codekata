try:
	p=int(input())
	if(p>=-2**15+1  and p<=2**15+1):
	    print ("INT")
	elif p>=-2**31+1 and p<=2**31+1:
	    print("LONG")  
	else:
	    print ("LONG LONG")
except ValueError:
	print("invalid")