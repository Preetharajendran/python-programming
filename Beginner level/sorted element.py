a1=int(raw_input())
a2=raw_input().split()
a2=map(int,a2)
if(a1==len(a2)):
  n=sorted(a2)
  for i in n:
    print i,
