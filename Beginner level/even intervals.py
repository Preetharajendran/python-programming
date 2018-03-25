n1,n2=raw_input().split()
b=[]
for n in range(int(n1)+1,int(n2)):
    if(n%2==0):
     b.append(n)
for i in b:
      print i,
