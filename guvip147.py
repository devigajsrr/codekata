no=list(map(str,input().split()))
s=""
for i in range(1,len(no)-1):
    k=list(no[i])
    no[i]="".join(k[::-1])
print(*no)
