N=input()
o =len(N)
if o > 1:
   for i in range(2, o):
       if (o % i) == 0:
           print("no")
           break
   else:
       print("yes")

else:
   print("no")