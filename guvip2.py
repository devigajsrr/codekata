o=int(input())
f=1
i=0
for i in range(o,0,-1):
    f=f*i
if o==0:
    print("1")
else:
    print(f)