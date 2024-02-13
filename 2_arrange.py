# Arrange string character such that lowercase letters should come first in another string.

a="aRe yoU Fine?"
b=""
for i in a:
    if i.islower():
        b = b + i

for i in a:
    if i.isupper():
        b=b+i

print(b)


c = a.split()
print(c)


