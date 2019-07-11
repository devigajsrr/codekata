o=list(map(str,input()))
o=o[::-1]
for i in range(0,len(o)):
    if i==len(o)-1: print(o[i])
    else: print(o[i],end="-")