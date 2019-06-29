import sys
m=list(input())
for i in range(0,len(m)):
    if m.count(m[i])>1:
        print("yes")
        sys.exit()
print("no")