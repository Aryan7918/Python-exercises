# write a python scripts to merge two python dictionaries.
# remeber about hard and soft copies
# dictionary is soft copy

a = {1:10,2:20,3:30,4:40}
b = {7:70,8:80,9:90}

# a.update(b)
# print(a)

c = a
c.update(b)
print(c)
print(a)