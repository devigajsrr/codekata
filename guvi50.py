x=int(input())
k=x
s=0
while x>1:
    if x%2==0:
        x=x/2
        s=s+1
    else:
        print("no")
        break
if (2**s)==k:
    print("yes")
