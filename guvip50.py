try:
	n=int(input())
	if n > 1: 
	   for iter in range(2, n//2): 
	       if (n % iter) == 0: 
	           print("yes") 
	           break
	   else: 
	       print("no") 
	else: 
	   print("yes") 
except ValueError:
	print("invalid")