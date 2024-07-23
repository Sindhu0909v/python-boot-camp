inp=input()
c=0
ans=""
for i in inp:
    if(i=='-'):
        c+=1
    else:
        ans=ans+i
print("-"*c+ans)