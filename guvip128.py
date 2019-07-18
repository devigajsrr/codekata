n=int(input())
p=list(map(int,input().split()))
if n==1:
    if n%2==0: print("even")
    else: print("odd")
else:
    if p[0]%2==0 and p[1]%2==0: print("even")
    else: print("no")
