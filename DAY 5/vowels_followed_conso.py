str=input()
l=str.lower()
str1=""
str2=""
vowels="aeiou"
conso="bcdfghjklmnpqrstvwxyz"
for i in l:
    if(i in vowels):
        str1+=i
#print(str1)
for i in l:
    if(i in conso):
        str2+=i
#print(str2)
print(str1+str2)