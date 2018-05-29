n1=int(raw_input())
n2=raw_input().split()
n2=map(int,n2)
i=0
if(n1==len(n2)):
  for n in n2:
    i=i+n
    c=i/n1
  print c
