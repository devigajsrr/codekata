str1,str2=input().split()
for j in range(0,len(str1)):
	if str1[j]==str2[j]:
		print("yes")
		break
else:
	print("no")