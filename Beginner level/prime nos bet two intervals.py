n1,n2=raw_input().split()
a=[]
for n in range(int(n1)+1,int(n2)):
    if(n>0):
        for i in range(2,n):
             if(n%i==0):
                break
        else:
            a.append(n)
for i in a:
     print i,
