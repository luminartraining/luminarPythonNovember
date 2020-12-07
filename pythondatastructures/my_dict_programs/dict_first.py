#values are stored in dictionary in the form of key,value pairs


# rol:100,name:ajay,course:bca
#rol,name,course


students={ 100:{"rol":100,"name":"ajay","course":"bca","total":150},
           101:{"rol":101,"name":"vjay","course":"mca","total":145},

          }#,array,queue(fifo),stack(lifo)(push,pop)


#python dict, java->Hashmap(),javascript-object,c-struct,
print(students[100])
# students["gender"]="male"
#cheking for a specific key
#print("rol" in students)
#
# students["total"]+=50
# print(students)

#print student name "ajay"
#ajay is a value, to fetch value we have to use corresponding key
# print(students["name"])
# #course
# print(students["course"])

# for key in students:
#     print(key,students[key])#rol,name,course
#


# for k,v in students.items():
#     print(k,v)
# students["name"]="AJAY"
# print(students)




#data structures
#how data is internally stored
lis=[10,20,30]
print(lis[1])
print(lis[2])

#1)linear datastructure data are stored in consecutive memory locations #,array,queue(fifo),stack(lifo)(push,pop)
#2)non linear datastructures linkedlist,tree


#