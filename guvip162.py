t=['a','e','i','o','u','A','E','I','O','U']
no,k=map(int,input().split())
l=[]
s=0
for i in range(no):
    r=list(input())
    for j in range(0,len(r)):
        if r[j] in t:
            s=s+1
            break
    l.append(r)
if s>=k:
    print("yes")
else: print("no")