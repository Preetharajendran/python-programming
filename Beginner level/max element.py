n1=int(raw_input())
n2=raw_input().split()
n2=map(int,n2)
if(n1==len(n2)):
  print max(n2)
