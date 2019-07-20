import sys
o=['a','b']
l=list(map(str,input()))
for i in range(0,len(l)):
    if l[i] not in o:
        print("no")
        sys.exit()
print("yes")
