vowels="aeiou"
conso="bcdfghjklmnpqrstvwxyz"
count=0
c=0
l=input()
inp=l.lower()
for i in inp:
    if(i in vowels):
        count+=1
for i in inp:
    if(i in conso):
        c+=1
print(count)
print(c)


