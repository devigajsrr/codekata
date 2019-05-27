o=str(input())
p=""
for i in o:
    if i.isupper():
        p=p+i.lower()
    else:
        p=p+i.upper()
print(p)
