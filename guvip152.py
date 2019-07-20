astr=input()
cnt=0
vow=["a","e","i","o","u"]
for i in range(0,len(astr)-2):
	if astr[i] in vow and astr[i+1] not in vow:
		cnt+=2
		if astr[i+1] not in vow and astr[i+2] in vow:
			cnt+=1
print(cnt)