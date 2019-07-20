no=list(map(str,input()))
d=[]
i=0
while i<(len(no)):
    d.append(no[i])
    d.append(str(no.count(no[i])))
    i=i+(no.count(no[i]))
s="".join(d)
print(s)