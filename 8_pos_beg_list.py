#4 print positive and negative elements of an list in seperates lists

a = [1,-6,-3,5,9,-2,5,-4]

pos = []
neg = []

for i in a:
    if i>0:
        pos.append(i)
    elif i<0:
        neg.append(i)

print(pos)
print(neg)
