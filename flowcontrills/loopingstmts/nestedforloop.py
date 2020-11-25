#1 to 12



#1 2 3 4
#5 6 7 8
#9 10 11 12

cnt=1
for i in range(1,13):#i=1,2,3 4,5
    print(i,end="\t")#1 2   3   4
                    #5
    if(cnt==4):
        print()
        cnt=1
    else:
        cnt+=1


