a=int(raw_input())
n=a
sum=0
while(a>0):
    b=a%10
    sum=sum*10+b
    a=a//10
if(n==sum):
    print("yes")
else:
    print("no")





