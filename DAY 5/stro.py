str=input()
lst="0123456789"
sum=0
for i in str:
    if(i in lst):
        sum+=int(i)
print(sum)


