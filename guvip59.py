num=int(input())
astr=input()
a=""
c1=""
for i in range(len(astr)):
	if astr[i]=="1":
		a=a+astr[i]+" "
	elif astr[i]=="0":
		c1=c1+a
		a=""
print(c1.strip())
