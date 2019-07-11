o,k=(map(str,input().split()))
o=list(o)
k=list(k)
if len(o)>len(k): o=o[0:len(k)]
elif len(o)<len(k): k = k[0:len(o)]
for i in range(0,len(k)): n.append(k[i])
for i in range(0,len(o)): print(o[i],end="")
