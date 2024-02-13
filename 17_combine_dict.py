#4 write a python program to combine two dictionary by adding values for common keys

a = {1:10,2:20,3:30,4:40}
b = {3:70,8:80,9:90,2:10}

for i in b.keys():
    if i in a.keys():
        a[i]=a[i]+b[i]
    else:
        a[i]=b[i]

print(a)