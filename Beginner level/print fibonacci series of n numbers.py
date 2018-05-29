a=int(raw_input())
n1=0
n2=1
for i in range(1,a+1):
  sum=n1+n2
  n1=n2
  n2=sum
  print n1,
