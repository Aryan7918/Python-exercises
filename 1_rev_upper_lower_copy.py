#1. Print string in reverse, its uppercase, lowercase, and copy into another string.

a="I am happy"
print(a[len(a)::-1])    # print(a[-1::-1])

print("length of the string",len(a))

print(a.upper())

print(a.lower())

b = a
print(b)