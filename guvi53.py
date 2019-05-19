x=int(input())
a=0
s=0
while x>0:
    a=x%10
    s=s+a
    x=x//10
print(s)
