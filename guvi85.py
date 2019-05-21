x=str(input())
for i in range(0,len(x)):
    if i%2==0:
        print(x[i],end="")
print(end=" ")
for i in range(0,len(x)):
    if i%2!=0:
        print(x[i],end="")
