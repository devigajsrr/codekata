o=list(map(int,input()))
x=0
for i in range(0,len(o)):
    if o[i]%2!=0:
        x=x+o[i]
if x%2==0: print("E")
else: print("O")