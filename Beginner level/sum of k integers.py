a1,a2=raw_input().split()
n1=raw_input().split()
if int(a1)==len(n1):
  n1=map(int,n1)
  n2=n1[0:int(a2)]
  print sum(k for k in n2)
