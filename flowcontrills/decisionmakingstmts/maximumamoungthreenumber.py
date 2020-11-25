num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
if((num1>num2)&(num1>num3)):
    print("num1 is max")
    if(num2>num3):
        print(num1,",",num2,",",num3)
    else:
        print(num1,",",num3,",",num2)


elif((num2>num1)&(num2>num3)):
    if(num1>num3):
        print(num2,",",num1,",",num3)
    else:
        print(num2, ",", num3, ",", num1)
        
elif((num3>num1)&(num3>num2)):
    if (num2> num1):
        print(num3, ",", num2, ",", num1)
    else:
        print(num3, ",", num1, ",", num2)

#second largest number

#print these three number in sorted order

#bday=15 byear=1992 bmonth=5  cday=17 cyear=2020 cmonth=11 calculate age 28years

