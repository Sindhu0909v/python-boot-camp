str=input()
num="0123456789"
for i in str:
    if(i in num):
        rev=0
        while(int(i)>0):
           d=int(i)%10
           rev=int(rev)*10+d
           i=int(i)//10
print(rev)

    