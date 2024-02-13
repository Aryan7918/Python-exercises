# find the second largest element and print its its index too.
# [2,96,69,77,145,20]
# Second Max=96 and at 1 index  

a = [2,96,69,77,145,20]
max=0
max2=0
index=index2=0

for i in range(len(a)):
    if a[i]>max:
        max2=max
        max=a[i] 
        index2=index
        index=i
    elif a[i]>max2:
        max2=a[i]
        index2=i
print(max2,index2)
