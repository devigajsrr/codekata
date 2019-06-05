try:
	num=int(input())
	lst3=[]
	s=""
	list1=list(map(int,input().split()))
	list2=list(map(int,input().split()))
	for i in list1:
		if i in list2 and i not in lst3:
			lst3.append(i)
	for i in lst3:
		s=s+str(i)+" "
	print(s.strip())	
except ValueError:
	print("invalid")