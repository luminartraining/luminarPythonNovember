#prime number?   7 (1,7) 7 is a prime number
#7

#1,7 exclude
number=int(input("enter number"))
flag=0
for i in range(2,number):#2
    if(number%i==0):
        flag=1
        break
    else:
        flag=0
if(flag==0):
    print("prime number")
else:
    print("not prime number")


#read low limit read upperlimit (10,50) print all primenumber from 10-50





