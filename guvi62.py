s=str(input())
x=0
for i in range(0,len(s)):
    if (s[i]!='0') and (s[i]!='1'):
        x=x+1
if x>0:
    print("no")
else: 
    print("yes")