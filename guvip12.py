import sys, string, math
c,b = map(int,input().split())
b = b%c
L1 = list(map(int,input().split()))
L2 = L1[-b:] + L1[:-b]
print(*L2)