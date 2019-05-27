K=input()
for k in K:
	A=K.count('(')
	B=K.count(')')
if A==B:
	print("yes")
else:
	print("no")
