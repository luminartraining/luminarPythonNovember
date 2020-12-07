f=open("complete.csv")

dict={}
for lines in f:

    #2020-01-30,Kerala,10.8505,76.2711,1.0,0,0.0,0,0,0
    data=lines.rstrip("\n").split(",")

    state=data[1]
    confirmed_cases=data[4]
    if state not in dict:
        dict[state]=int(float(confirmed_cases))
    else:
        dict[state] = int(float(confirmed_cases))
for k,v in dict.items():
    print(k,v)


highest=max(dict,key=dict.get)
print("highest",highest,dict[highest])

lowes=min(dict,key=dict.get)
print(lowes,dict[lowes])



srt=sorted(dict,key=dict.get,reverse=True)
print("sorted",srt)

#find state which have highest confirmed_cases
#find state which have lowest confirmed_cases
#sort the states depends on confirmed cases