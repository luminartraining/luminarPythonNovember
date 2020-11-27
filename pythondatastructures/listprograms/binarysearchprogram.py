lst=[7,2,3,6,8,1,10]
#step 1
lst.sort()

element=int(input("enter the element you want to search"))
print(lst)


low=0
upp=len(lst)-1
flg=0
while(low<upp):
    mid=(low+upp)//2
    #case1
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flg=1
        break
if(flg>0):
    print("element found")
else:
    print("element not found")