num=int(raw_input())
n1=str(num)
b=len(n1)
sum = 0
temp = num
while(temp > 0):
   digit = temp % 10
   sum += digit **b
   temp //= 10
if(num == sum):
   print "yes"
else:
   print "no"
