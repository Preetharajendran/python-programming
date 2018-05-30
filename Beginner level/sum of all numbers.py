a1=int(raw_input())
n1=raw_input().split()
if int(a1)==len(n1):
  n1=map(int,n1)
  print sum(k for k in n1)
