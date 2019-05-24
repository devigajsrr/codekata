o=list(map(str,input()))
t=""
for i in range(0,len(o)-1,2):
    t=o[i]
    o[i]=o[i+1]
    o[i+1]=t
for i in range(0,len(o)):
    print(o[i],end="")
