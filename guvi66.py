x=int(input())
s=0
for i in range(2,x):
    if x%i==0:
        s=1
if s==0:
    print("yes")
else: print("no")
