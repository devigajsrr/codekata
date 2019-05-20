o,p=map(int,(input().split()))
s=abs(o-p)
x=s%2
if x==0:
    print("even")
else:
    print("odd")
