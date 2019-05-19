x,y=input().split()
if(x.isdigit()==True and y.isdigit()==True):
  x=int(x)
  y=int(y)
x=x^y
y=x^y
x=x^y
print(x,y)
