n=int(raw_input())
import random
min = 1
max = 4
max1=6
max2=12
max3=18
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print "rolling the dice are"
    print "the values are"
    if(n==4):
      print random.randint(min,max)
      roll_again=raw_input("roll the dice again")
    elif(n==6):
      print random.randint(min,max1)
      roll_again=raw_input("roll the dice again")
    elif(n==12):
      print random.randint(min,max2)
      roll_again=raw_input("roll the dice again")
    elif(n==18):
      print(min,max3)
      roll_again=raw_input("roll the dice again")
    
