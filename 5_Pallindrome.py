a = "12321"
# print(a==a[-1::-1])
b=""
for i in range(len(a)-1,-1,-1):
    b = b + a[i]

if a==b:
    print(f"{b} is Pallindrome")
else:
    print(f"{b} is not Pallindrome")    
