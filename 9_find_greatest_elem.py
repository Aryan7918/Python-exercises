# find the greatest element and print its index too.
# [2,96,69,77,145,20]
# Max = 145 at 4 index

a = [2,96,69,77,145,20,25,36]
max = 0
index = 0
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
        index=i
print(f"Maximum element is {max} at index {index}")
