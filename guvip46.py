import math
try:
	anglee=int(input())
	radian=anglee*(math.pi/180)
	if radian<1 and radian>0:
		print(round(math.sin(radian),1))
	else:
		print(round(math.sin(radian)))
except ValueError:
	print("invalid")