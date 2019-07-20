import sys
o=int(input())
for i in range(0,1000):
    if 2**i==o: 
        print("yes")
        sys.exit()
print("no")
