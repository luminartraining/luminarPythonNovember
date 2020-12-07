#file operations Read r,write w,append a



#step1 create refernce
#reference_name=open(filepath,mode_of_operation)

f=open("names","r")
lst=[]
for lines in f:
    lst.append(lines.rstrip("\n"))
print(lst)