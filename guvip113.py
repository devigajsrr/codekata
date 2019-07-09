s=list(map(int,input().split("/")))
if 0<s[0]<32 and 0<s[1]<13 and s[2]>1200 and len(s)==3: print("yes")
else: print("no")