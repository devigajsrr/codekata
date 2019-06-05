str1,str2,n=input().split()
str1=str(str1)
str2=str(str2)
n=int(n)
count=0
for i in range(0,len(str1)):
	if(str1[i]!=str2[i]):
		count+=1
	else:
		continue
if(count==n):
	print("yes")
else:
	print("no")