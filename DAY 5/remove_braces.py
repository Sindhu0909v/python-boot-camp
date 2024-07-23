''''str=input()
str2=""
#check="40,41,91,93,123,125"
for i in str:
    if( i in ):
        pass
    else:
        str2+=i
print(str2)'''

str=input()
for i in str:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end="")
print()
