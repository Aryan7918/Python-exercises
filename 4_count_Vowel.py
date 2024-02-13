# count vowels from given string
a="I am aryan patel"
vowel=conso=digit=0
for i in a:
    if i in "aeiouAEIOU":
        vowel = vowel + 1
    elif i in " ":
        continue
    else:
        conso = conso + 1
print(vowel)
print(conso) 
