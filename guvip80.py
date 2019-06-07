try:
	num=map(int,input().split())
	l=[int(x) for x in input().split()]
	ar=[]
	for i in range(0,len(l)-1):
		for j in range(i+1,len(l)):
			if l[i]-l[j]!=0:
				ar.append(abs(l[i]-l[j]))
	print(min(ar))
except ValueError:
	print("invalid")