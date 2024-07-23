str=input()
sum=0
c=0
for i in str:
    if(i.isdigit()):
        c=int(i)
        sum+=c
print(sum)