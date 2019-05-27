N,K=map(int,input().split())
list=list(map(int,input().split()))
for k in list:
  if k==K:
    print("Yes")
    break
else:
  print("No")