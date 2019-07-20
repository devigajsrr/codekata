import sys
no=int(input())
l=[]
for i in range(0,no):
    d=input()
    l.append(d)
for i  in range(0,no-1):
    if l[i]==l[i+1]:
        print("yes")
        sys.exit()
print("no")
