#3 Print list elements in reverse order

a = [10,20,3,0,50,46]
b = []
for i in range(len(a)-1,-1,-1):
    b.append(a[i])

print(b)