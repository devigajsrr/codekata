x,y=map(int,input().split())
for n in range(x+1,y):
    t = n
    r = 0
    while (n > 0):
        d = n % 10
        r = r + d ** 3
        n = n // 10
    if (t == r):
        print(t, end=" ")