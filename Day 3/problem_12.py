'''max elem in a given list'''
lst=list(map(int,input().split()))
m=lst[0]
for i in range(0,len(lst)):
    if(m<lst[i]):
        m=lst[i]
print(m)
