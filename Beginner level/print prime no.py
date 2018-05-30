n1=int(raw_input())
if(n1>0):
 for i in range(2,n1):
   if(n1%i==0):
     print ("no")
     break
 else:
     print "yes"
else:
 print("invalid")
