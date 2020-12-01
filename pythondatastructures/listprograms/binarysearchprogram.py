lst=[7,2,3,6,8,1,10]
#step 1
lst.sort()

element=int(input("enter the element you want to search"))
print(lst)


low=0
upp=len(lst)-1
flg=0
#       e
#[1, 2, 3, 6, 7, 8, 10]
#l       m           u
while(low<=upp):#0<6
    mid=(low+upp)//2#2
    #case1
    if(element>lst[mid]): #3>3
        low=mid+1
    elif(element<lst[mid]):#3<3
        upp=mid-1
    elif(element==lst[mid]):#3==3
        flg=1
        break
if(flg>0):
    print("element found")
else:
    print("element not found")