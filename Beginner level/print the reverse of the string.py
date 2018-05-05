str=raw_input()
n=len(str)
rev=""
while n!=0:
    rev=rev+str[n-1]
    n=n-1
print(rev)
