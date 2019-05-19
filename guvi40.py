x=input()
x=int(x)
n1=1
n2=1
if(x==1):
    print(n1,end='')
count=0
if(x>1):
    while(count<x):
        if(count==x-1):
            print(n1,end='')
        else:
            print(n1,end=' ')
        nth=n1+n2
        n1=n2
        n2=xth
        count=count+1