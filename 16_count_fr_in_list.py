#3 count the frequeny of each elements in a list

a=[1,1,2,3,4,5,6,6,3,5,6,5,6,5,6,2,3,2,5,5,2,3,5,]

dict = {}

for i in a:
    if i in dict.keys():
        dict[i]= dict[i]+1
    else:
        dict[i]= 1 

print(dict)