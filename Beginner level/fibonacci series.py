n=int(raw_input())
t1=0
t2=1
for i in range(1,n+1):
  sum=t1+t2
  t1=t2
  t2=sum
  print t1,
