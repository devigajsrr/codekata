try:
	peri,a=map(int,input().split())
	h=int(peri/2)
	if(h*2==peri):
		if a > 1:
			for iter in range(2, a//2):
				 if (a % iter) == 0: 
				 	print("yes")
				 	break
			else:
				print("no")
		else:
			print("yes")
	else:
		print("no")
except ValueError:
	print("invalid")