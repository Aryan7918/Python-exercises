# 7 palindrome list write a program to check if elements of an list are same or not it read from front or back
# example : arr = [2,3,15,15,3,2]
a=[1,2,3,2,1]
b=[]

for i in range(len(a)-1,-1,-1):
    b.append(a[i])

if a==b:
    print("palindrome")
else:
    print("not a palindrome")