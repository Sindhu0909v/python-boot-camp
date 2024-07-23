'''print the non repeating charcters in a string'''
str=input()
str2=""
for i in str:
    if(i not in str2):
        str2+=i
print(str2)