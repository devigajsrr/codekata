no,k=map(str,input().split())
no=list(no)
k=int(k)
no=no[k-1:len(no):k]
print(*no)