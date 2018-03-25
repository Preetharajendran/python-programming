n1,n2=raw_input().split()
p=[]
for num in range (int(n1)+1,int(n2)):
    a=str(num)
    b=len(a)
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit **b
       temp //= 10
    if num == sum:
        p.append(num)
for i in p:
    print i,
