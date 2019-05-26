import re
O=int(input())
Z=input()
T=re.sub('[aeiou]','',Z)
print(T[::-1])