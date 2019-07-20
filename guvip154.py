no,k=map(str,input().split())
no=list(no)
k=int(k)
x="a"
for i in range(k-1,len(no),k):
    x=str(no[i])
    no[i]=x.upper()
for i in range(0,len(no)): print(no[i],end="")
