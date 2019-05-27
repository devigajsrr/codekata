m,a=map(int,input().split(" "))
n,b=map(int,input().split(" "))
o,c=map(int,input().split(" "))
if(m==n==o):
    print("yes")
elif(a==b==c):
    print("yes")
elif(m==a and n==b and o==c):
    print("yes")
else:
    print("no")
