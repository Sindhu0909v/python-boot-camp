'''given a space sep int list...find the avg of elements present in the even index'''
lst=list(map(int,input().split()))
sum=0
c=0
for i in range(0,len(lst)):
    if(i%2==0):
        sum+=lst[i]
        c+=1
print("average=",(sum/c))