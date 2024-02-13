# Count all letters, digits, and special symbols from a given string
# str1 = "P@#yn26at^&i5ve"
# expected outcome: 
# chars = 8
# digits = 3
# symbols = 4 

str1 = "P@#yn26at^&i5ve"

ch=sy=dg= 0

for i in str1:
    if i.isalpha():
        ch = ch + 1
    elif i.isdigit():
        dg = dg + 1
    else:
        sy = sy + 1

print( ch ,dg,sy )