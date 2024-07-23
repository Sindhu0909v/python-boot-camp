str=input()
str1=""
str2=""
#rev=0
for i in str:
    if(i.isaplha()):
        str2+=i
    if(i.isdigit()):
        str2+=i
        str2=str2[::-1]
print(str1+str2)    
