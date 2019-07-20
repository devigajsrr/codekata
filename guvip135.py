o=int(input())
l=list(map(int,input().split()))
if o%2==0: x=o/2
else: x=(o-1)/2
k=l[0:int(x)]
k=sorted(k)
m=l[int(x):o]
m=sorted(m)
m=m[::-1]
for i in range(len(m)): k.append(m[i])
print(*k)