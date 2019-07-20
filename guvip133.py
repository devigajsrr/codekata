import sys
o,k=map(int,input().split())
l=[]
for i in range(0,o):
    l.append(list(map(int,input().split())))
for i in range(0,o):
    if l[i][1]==k:
        print("yes")
        sys.exit()
print("no")