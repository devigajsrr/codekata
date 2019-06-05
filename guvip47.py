import math
try:
	a1,a2,a3=map(int,input().split())
	if((a1+a2+a3)==180 and a1!=0 and a2!=0 and a3!=0):
		print("yes")
	else:
		print("no")
except ValueError:
	print("invalid")