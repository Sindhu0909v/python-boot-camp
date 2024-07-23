'''peak element
lst=list(map(int,input().split()))
for i in range(1,len(lst)-1):
    if(lst[i-1]<lst[i] and lst[i+1]<lst[i]):
        peak=lst[i]
        print(peak)'''
lst=list(map(int,input().split()))
c=0
for i in range(1,len(lst)-1):
    if(lst[i-1]<lst[i] and lst[i+1]<lst[i]):
        c=i
        #print(lst[i],end=" ")
if(lst[-1]>lst[-2] and lst[-1]>c):
    c+=len(lst)-1
print(lst[c])
