o=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(len(l)+1):
    for j in range(i+1,len(l)+1):
        a.append(l[i:j])
print(len(a))