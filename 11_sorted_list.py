# check list is in sorted order or not
a=[1,2,3,4,9,5,6]

for i in range(len(a)-1):
    if a[i] <= a[i+1]:
        continue
    else: 
        print("your list is not sorted")
        break
else:
    print("your list is sorted")
