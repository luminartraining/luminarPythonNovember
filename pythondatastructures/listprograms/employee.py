employees=[[1001,"ajay","qa",15000],
        [1002,"vijay","developer",25000],
        [1003,"arun","ba",15000],
        [1004,"amal","developer",30000]]
#print all employee id


#find total of salary



#find how many mebers working as developer

#find total of salary  group by designation
# qasum=0
# dsum=0
# for employee in employees:
#     if(employee[2]=="qa"):
#         qasum+=employee[3]
#     elif (employee[2] == "developer"):
#         dsum += employee[3]
#
employees=[[1001,"ajay","qa",1981,2003],
        [1002,"vijay","developer",1992,2008],
        [1003,"arun","ba",1989,2010],
        [1004,"amal","developer",2009,2014],
        [1004,"vimal","developer",1987,1989]
           ]
#print all employee designation
#print all employee whose desig =developer

#print all employees those who are working in 1980's


#print all employee details whose experience > 9 years

for emp in employees:
        #[1001,"ajay","qa",1981,2003]
        # if((emp[4]-emp[3])>9):
        #         print(emp)
        #
        if(emp[2]=='developer'):
                print(emp)


# pattern="ABABA"
#find find first recursive character A